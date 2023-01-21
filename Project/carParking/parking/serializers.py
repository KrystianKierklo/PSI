from rest_framework import serializers
from .models import Car, Carowner, Parkingplaces
from datetime import datetime
from django.contrib.auth.models import *
from django import *
from django.contrib.auth.models import User


class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.registrynumber')
    class Meta:
        model = Car
        fields = ['registrynumber', 'vehicalbrand', 'vehicalmodel', 'productionyear', 'color', 'owner']

class Carownerserializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    class Meta:
        model = Carowner
        fields = ['phone_number', 'name', 'lastname', 'email', 'adress', 'carregistrynumber', 'owner']

    # def validate_name(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Imię nie może być puste",)
class Parkingplacesserializer(serializers.HyperlinkedModelSerializer):
    dateofpurchase = serializers.DateTimeField()
    class Meta:
        model = Parkingplaces
        fields = ['placenumber', 'car_registrynumber', 'dateofpurchase']


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['url', 'vehicalbrand', 'vehicalmodel', 'registrynumber']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cars = UserCarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url','pk', 'cars']