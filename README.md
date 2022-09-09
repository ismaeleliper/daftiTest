# Dafti Assessment Project
 ##### This is a simple service created with the Python/Django Framework and Django Rest Framework, on the purpose to show a litle of my abilities with the tecnology.

 ###### The Service is a Shoes Manager or just a CRUD.

![Badge Done](http://img.shields.io/static/v1?label=STATUS&message=Done&color=GREEN&style=for-the-badge)

### To run locally:
     - Docker>==20.10.17
     - docker-compose>==1.29.4

     - $ git clone https://github.com/ismaeleliper/daftiTest.git

        (!) Verify if the ports 8000 and 5432 are available before giving next commands

     - $ docker-compose up -d --build

     - Create a superuser to login
     - $ docker exec -it <web container-id> python3 web/manage.py createsuperuser
        - Access http://localhost:8000/admin/shoes/shoes
        - Access http://localhost:8000/api-shoes

     To run tests:
        - $ docker exec -it <web container-id> python3 web/manage.py test shoes


 --------------------------------------------------------------------------------------------------------- 

## Simple Documentation:

### - POST: /api-shoes/create
    - Content-Type: application/json    
Field         | Type      | Description
------------- |-----------| ------------- 
Model  | Charfield (200) | The model of Shoes
Brand  | Charfield (200) | The brand of Shoes  
Quantity  | Integer   | The total of Shoes in stock  
Price  | Decimal   | The unitary price of Shoes   
    
    - Required Payload:
    {
        "model": "Yeezy",
        "brand": "Adidas",
        "quantity": 2,
        "price": 200
    }
    
    - Response Expected:

        {
            "uuid": "ff2c24d1-747b-4e42-b540-ba79dd2f2b9c",
            "model": "Yeezy",
            "brand": "Adidas",
            "quantity": 2,
            "price": 200
        }

### - GET: /api-shoes/all
    - Reponse Expected:

        [
            {
                "uuid": "ff2c24d1-747b-4e42-b540-ba79dd2f2b9c",
                "model": "Yeezy",
                "brand": "Adidas",
                "quantity": 2,
                "price": 200
            }
        ]

### - PUT: /api-shoes/update/[uuid] 
        - Content-Type: application/json
        - uuid - has to be a valid Shoes uuid, otherwise it will return a 404
Field         | Type      | Description
------------- |-----------| ------------- 
Model  | Charfield (200) | The model of Shoes
Brand  | Charfield (200) | The brand of Shoes  
Quantity  | Integer   | The total of Shoes in stock  
Price  | Decimal   | The unitary price of Shoes   
    
    - Required Payload:
    {
        "model": "Yeezy 2 ",
        "brand": "Adidas",
        "quantity": 2,
        "price": 200
    }
    
    - Response Expected:

        {
            "uuid": "ff2c24d1-747b-4e42-b540-ba79dd2f2b9c",
            "model": "Yeezy 2 ",
            "brand": "Adidas",
            "quantity": 2,
            "price": 200
        }

### - DELETE: /api-shoes/delete/[uuid]
        - uuid - has to be a valid Shoes uuid, otherwise it will return a 404


    
    - Response Expected:

        - STATUS CODE 202

<br/>
<hr>
<footer>
    <p style="awidth: 20%;">Copyright © Ismael Eliabe, 2022</p>
</footer>
