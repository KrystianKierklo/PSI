from django.contrib import admin
from.models import Car, Carowner, Parkingplaces
from rest_framework.pagination import LimitOffsetPagination
# Register your models here.

# admin.site.register(Car)
# admin.site.register(Carowner)
# admin.site.register(Parkingplaces)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ['productionyear']

@admin.register(Carowner)
class CarownerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'lastname']
    list_display = ['id', 'name', 'lastname' , 'carregistrynumber' ]
    list_filter = ['lastname']

@admin.register(Parkingplaces)
class ParkingplacesAdmin(admin.ModelAdmin):
    pass


