from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
import datetime

def validate_phone_number(value):
    if len(value) != 9:
        raise ValidationError(_("Numer telefonu musi składać się z 9 cyfr"))
    return value

def validate_productionyear(value):
    data = datetime.date.today()
    year = data.year
    if value > year:
        raise ValidationError(_("Podałeś rok którego jeszcze nie mieliśmy"))
    return value

def validate_placenumber(value):
    if value < 0 or value > 150:
        raise ValidationError(_("Niewłaściwy numer miejsca parkingowego"))
    return value

# def validate_dateofpurchase(value):
#     data = datetime.date.today()
#     if value > data:
#         raise ValidationError(_("Niewłaściwa data"))
#     return value

def validate_email(value):
    for i in value:
        if i == "@":
            return value
    raise ValidationError(_("Niewłaściwy adres email"))
class Car(models.Model):
    registrynumber = models.CharField(max_length=10)
    vehicalbrand = models.CharField(max_length=50)
    vehicalmodel = models.CharField(max_length=50)
    productionyear = models.IntegerField(validators=[validate_productionyear])
    color = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicalbrand} {self.vehicalmodel} {self.registrynumber}"


class Parkingplaces(models.Model):
    placenumber = models.IntegerField(validators=[validate_placenumber])
    car_registrynumber =models.ForeignKey(Car, on_delete=models.CASCADE)
    dateofpurchase = models.DateTimeField()
    def __str__(self):
        return f'{self.placenumber}'


class Carowner(models.Model):

    phone_number = models.CharField(max_length=9, validators=[validate_phone_number])
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45, validators=[validate_email])
    adress = models.CharField(max_length=120)
    carregistrynumber = models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}  {self.lastname}"