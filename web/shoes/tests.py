import json
from uuid import UUID, uuid4
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse

from .models import Shoes


class ShoesModelsTestCase(TestCase):
    def setUp(self):
        Shoes.objects.create(
            uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f'),
            model="Yeezy",
            brand="Adidas",
            price=1000,
            quantity=200
        )

    def test_shoes_get(self):
        yeezy = Shoes.objects.get(uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f'))
        self.assertEqual(yeezy.brand, 'Adidas')

    def test_shoes_update(self):
        Shoes.objects.filter(uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f')).update(
            price=2000
        )
        self.assertEqual(
            Shoes.objects.get(uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f')).price,
            2000
        )

    def test_shoes_delete(self):
        Shoes.objects.filter(uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f')).delete()
        self.assertFalse(Shoes.objects.filter(uuid=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f')).exists())


class ShoesEndpointsTestCase(APITestCase):
    def setUp(self):
        self.valid_payload = json.dumps({
            "model": "Air",
            "brand": "Nike",
            "quantity": 5,
            "price": 500
        })
        self.invalid_payload = json.dumps({
            "model": "Air",
            "brand": "Nike",
            "quantity": "",
            "price": 500
        })

    def url(self, suffix: str, args: list = None):
        if args:
            return reverse(f"shoes:{suffix}", args=args)
        else:
            return reverse(f"shoes:{suffix}")

    def test_create_shoes(self):
        response = self.client.post(
            self.url("add-shoes"),
            data=self.valid_payload,
            content_type="application/json"
        )
        self.assertEqual(response.json()["model"], "Air")
        self.assertEqual(response.json()["brand"], "Nike")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_shoes_invalid_payload(self):
        with self.assertRaises(ValueError):
            self.client.post(
                self.url("add-shoes"),
                data=self.invalid_payload,
                content_type="application/json"
            )

    def test_retrieve_shoes(self):
        counter = 0
        for shoes in range(10):
            Shoes.objects.create(
                uuid=uuid4(),
                model=f"Yeezy{counter}",
                brand=f"Adidas-version-{counter}",
                price=1000,
                quantity=200
            )
            counter += 1
        response = self.client.get(self.url("view-shoes"), )
        self.assertEqual(len(response.json()), 10)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_shoes(self):
        Shoes.objects.create(
            uuid=UUID('444519e6-108b-450c-849a-af7225f02112'),
            model="Yeezy",
            brand="Adidas",
            price=1000,
            quantity=200
        )
        response = self.client.put(
            self.url("update-shoes", args=['444519e6-108b-450c-849a-af7225f02112']),
            data=json.dumps({
                "model": "Air",
                "brand": "Nike",
                "quantity": 5,
                "price": 500
            }),
            content_type="application/json"
        )
        self.assertEqual(response.json(), {'uuid': '444519e6-108b-450c-849a-af7225f02112',
                                           'model': 'Air',
                                           'brand': 'Nike',
                                           'quantity': 5,
                                           'price': '500.00000'})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_shoes(self):
        Shoes.objects.create(
            uuid=UUID('5c96fc02-4d5a-4bf1-b404-cd31f2b84710'),
            model="Yeezy 2",
            brand="Adidas",
            price=1000,
            quantity=200
        )
        response = self.client.delete(self.url("delete-shoes", args=['5c96fc02-4d5a-4bf1-b404-cd31f2b84710']))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
