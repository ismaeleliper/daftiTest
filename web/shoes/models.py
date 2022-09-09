from django.db import models
from uuid import UUID


class Shoes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=UUID('b3aa7316-7e74-4480-8b45-cd5220fd020f'), editable=False)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"{self.brand} {self.model}"
