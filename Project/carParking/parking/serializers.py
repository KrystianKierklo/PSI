from rest_framework import serializers
from .models import Car, Carowner, Parkingplaces

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['registrynumber', 'vehicalbrand', 'productionyear']

class Carownerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carowner
        fields = ['idcarowner', 'name', 'lastname', 'email', 'adress', 'carregistrynumber']

class Parkingplacesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parkingplaces
        fields = ['placenumber', 'car_registrynumber', 'dateofpurchase']

