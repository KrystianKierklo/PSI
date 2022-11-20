from django.db import models

# Create your models here.



class Car(models.Model):
    registrynumber = models.CharField(max_length=10)
    vehicalbrand = models.CharField(max_length=50)
    vehicalmodel = models.CharField(max_length=50)
    productionyear = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.registrynumber


class Parkingplaces(models.Model):
    placenumber = models.IntegerField()
    car_registrynumber =models.ForeignKey(Car, on_delete=models.CASCADE)
    dateofpurchase = models.DateTimeField()
    def __str__(self):
        return self.placenumber


class Carowner(models.Model):
    idcarowner = models.IntegerField()
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=120)
    carregistrynumber = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}  {self.lastname}"