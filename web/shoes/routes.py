from django.urls import path
from . import api

app_name = "shoes"

urlpatterns = [
    path("", api.overview, name='overview'),
    path("create/", api.create, name='add-shoes'),
    path("all/", api.retrieve, name='view-shoes'),
    path("update/<str:uuid>/", api.update, name='update-shoes'),
    path("delete/<str:uuid>/", api.delete, name='delete-shoes'),
]
