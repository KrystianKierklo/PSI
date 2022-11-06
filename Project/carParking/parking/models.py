from django.db import models

# Create your models here.



class car(models.Model):
    registrynumber = models.CharField(max_length=10)
    vehicalbrand = models.CharField(max_length=50)
    vehicalmodel = models.CharField(max_length=50)
    productionyear = models.IntegerField()
    color = models.CharField(max_length=50)


class parkingplaces(models.Model):
    placenumber = models.IntegerField()
    car_registrynumber =models.ForeignKey(car.registrynumber)
    dateofpurchase = models.DateTimeField()


class carowner(models.Model):
    idcarowner = models.IntegerField()
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=120)
    carregistrynumber = models.ForeignKey(car.registrynumber)