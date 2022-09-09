from uuid import UUID
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Shoes
from .serializer import ShoesSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def overview(request):
    return Response(
        {
            "urls": [
                "api-shoes/create",
                "api-shoes/all",
                "api-shoes/update/<uuid>",
                "api-shoes/delete/<uuid>"
            ],
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def create(request):
    shoes = ShoesSerializer(data=request.data)

    # validating for already existing data
    if Shoes.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if shoes.is_valid():
        shoes.save()
        return Response(shoes.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def retrieve(request):
    if request.query_params:
        shoes = Shoes.objects.filter(**request.query_param.dict())
    else:
        shoes = Shoes.objects.all()

    if shoes:
        data = ShoesSerializer(shoes, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update(request, uuid):
    try:
        shoes = Shoes.objects.get(uuid=UUID(uuid))
        data = ShoesSerializer(instance=shoes, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request, uuid):
    try:
        shoes = get_object_or_404(Shoes, uuid=UUID(uuid))
        shoes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

