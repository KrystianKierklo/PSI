from rest_framework import serializers
from .models import Car, Carowner, Parkingplaces
from datetime import datetime
from django.contrib.auth.models import *
from django import *

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['registrynumber', 'vehicalbrand', 'vehicalmodel', 'productionyear', 'color']

class Carownerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carowner
        fields = ['phone_number', 'name', 'lastname', 'email', 'adress', 'carregistrynumber']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Imię nie może być puste",)
class Parkingplacesserializer(serializers.HyperlinkedModelSerializer):
    dateofpurchase = serializers.DateTimeField()
    class Meta:
        model = Parkingplaces
        fields = ['placenumber', 'car_registrynumber', 'dateofpurchase']

