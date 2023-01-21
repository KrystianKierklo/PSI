from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Car, Carowner, Parkingplaces
from rest_framework import viewsets
from .serializers import CarSerializer, Carownerserializer, Parkingplacesserializer, UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import IsCurrentUserOwnerOrReadOnlu


def home(request):
    return HttpResponse("<h1>Witaj w mojej aplikacji</h1> aby przejść do widoków użyj /car /carowner /parkingplaces")

class CarFilter(FilterSet):
    from_year = DateTimeFilter(field_name='productionyear', lookup_expr='gte')
    to_year = DateTimeFilter(field_name='productionyear', lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['from_year', 'to_year']
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    name = 'carList'
    search_fields = ['vehicalmodel']
    ordering_fields = ['productionyear']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnlu)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnlu)
    name = 'car-detail'


class CarownerList(generics.ListCreateAPIView):
    queryset = Carowner.objects.all()
    serializer_class = Carownerserializer
    name = 'carownerList'
    filterset_fields = ['lastname']
    search_fields = ['lastname']
    ordering_fields = ['lastname']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnlu)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarownerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carowner.objects.all()
    serializer_class = Carownerserializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnlu)
    name = 'carowner-detail'


class ParkingplacesList(generics.ListCreateAPIView):
    queryset = Parkingplaces.objects.all()
    serializer_class = Parkingplacesserializer
    name = 'parkingplacesList'
    search_fields = ['placenumber']
    ordering_fields = ['placenumber', 'dateofpurchase']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParkingplaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parkingplaces.objects.all()
    serializer_class = Parkingplacesserializer
    name = 'parkingplace-detail'
    permission_classes = (permissions.IsAdminUser,)





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'car': reverse(CarList.name, request=request),
                         'carowner': reverse(CarownerList.name, request=request),
                         'parkingplaces': reverse(ParkingplacesList.name, request=request),
                         'users': reverse(UserList.name, request=request)
})