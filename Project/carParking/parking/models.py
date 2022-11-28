from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_phone_number(value):
    if len(value) != 9:
        raise ValidationError(_("Numer telefonu musi składać się z 9 cyfr"))
    return value

class Car(models.Model):
    registrynumber = models.CharField(max_length=10)
    vehicalbrand = models.CharField(max_length=50)
    vehicalmodel = models.CharField(max_length=50)
    productionyear = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vehicalbrand} {self.vehicalmodel} {self.registrynumber}"


class Parkingplaces(models.Model):
    placenumber = models.IntegerField()
    car_registrynumber =models.ForeignKey(Car, on_delete=models.CASCADE)
    dateofpurchase = models.DateTimeField()
    def __str__(self):
        return f'{self.placenumber}'


class Carowner(models.Model):

    phone_number = models.CharField(max_length=9, validators=[validate_phone_number])
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=120)
    carregistrynumber = models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}  {self.lastname}"