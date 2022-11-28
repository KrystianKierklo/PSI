from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers
from .views import CarViewSet, CarownerViewSet, ParkingplacesViewSet



router = routers.DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'owner', CarownerViewSet)
router.register(r'place', ParkingplacesViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
]
