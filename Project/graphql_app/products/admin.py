from django.contrib import admin
from .models import Car, Carowner, Parkingplaces
# Register your models here.


admin.site.register(Car)
admin.site.register(Carowner)
admin.site.register(Parkingplaces)