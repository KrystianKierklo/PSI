from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register(r'car', CarList)
router.register(r'owner', CarownerList)
router.register(r'place', ParkingplacesList)


urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('car', views.CarList.as_view(), name=views.CarList.name),
    path('car/<int:pk>', views.CarDetail.as_view(), name=views.CarDetail.name),
    path('carowner', views.CarownerList.as_view(), name=views.CarownerList.name),
    path('parkingplaces', views.ParkingplacesList.as_view(), name=views.ParkingplacesList.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name= views.UserDetail.name),
]
