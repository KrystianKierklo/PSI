from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Carowner, Parkingplaces
from rest_framework import viewsets
from .serializers import CarSerializer, Carownerserializer, Parkingplacesserializer


def home(request):
    return HttpResponse("Pierwszy widok")

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarownerViewSet(viewsets.ModelViewSet):
    queryset = Carowner.objects.all()
    serializer_class = Carownerserializer

class ParkingplacesViewSet(viewsets.ModelViewSet):
    queryset = Parkingplaces.objects.all()
    serializer_class = Parkingplacesserializer

