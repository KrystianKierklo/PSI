from .models import Car, Carowner, Parkingplaces
from graphene_django import DjangoObjectType
import graphene


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ('id', 'registrynumber', 'vehicalbrand', 'vehicalmodel', 'productionyear', 'color')


class CarownerType(DjangoObjectType):
    class Meta:
        model = Carowner
        fields = ('id', 'phone_number', 'name', 'lastname', 'email', 'adress', 'carregistrynumber')


class ParkingplacesType(DjangoObjectType):
    class Meta:
        model = Parkingplaces
        fields = ('id', 'placenumber', 'car_registrynumber', 'dateofpurchase')

class Query(graphene.ObjectType):
    cars = graphene.List(CarType)
    carowners = graphene.List(CarownerType)
    parkingplaces = graphene.List(ParkingplacesType)

    def resolve_cars(root, info, **kwargs):
        return Car.objects.all()

    def resolve_carowners(root, info, **kwargs):
        return Carowner.objects.all()

    def resolve_parkingplaces(root, info, **kwargs):
        return Parkingplaces.objects.all()




class UpdateCar(graphene.Mutation):
    class Arguments:
        color = graphene.String(required=True)
        id = graphene.ID()
    car = graphene.Field(CarType)
    @classmethod
    def mutate(cls, root, info, color, id):
        car = Car.objects.get(pk=id)
        car.color = color
        car.save()
        return UpdateCar(color=color)


class CreateCar(graphene.Mutation):
    class Arguments:
        registrynumber = graphene.String(required=True)
        vehicalbrand = graphene.String(required=True)
        vehicalmodel = graphene.String(required=True)
        productionyear = graphene.String(required=True)
        color = graphene.String(required=True)
    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, registrynumber, vehicalbrand, vehicalmodel, productionyear, color):
        car = Car()
        car.registrynumber = registrynumber
        car.vehicalbrand = vehicalbrand
        car.vehicalmodel = vehicalmodel
        car.productionyear = productionyear
        car.color = color
        car.save()
        return CreateCar(car=car)


class CarownerInput(graphene.InputObjectType):
    phone_number = graphene.String()
    name = graphene.String()
    lastname = graphene.String()
    email = graphene.String()
    adress = graphene.String()
    carregistrynumber = graphene.String()


class CreateCarowner(graphene.Mutation):
    class Arguments:
        input = CarownerInput(required=True)

    carowner = graphene.Field(CarownerType)

    @classmethod
    def mutate(cls, root, info, input):
        carowner = Carowner()
        carowner.phone_number = input.phone_number
        carowner.name = input.name
        carowner.lastname = input.lastname
        carowner.email = input.email
        carowner.adress = input.adress
        carowner.carregistrynumber = input.carregistrynumber
        carowner.save()
        return CreateCarowner(carowner=carowner)

class UpdateCarownernumber(graphene.Mutation):
    class Arguments:
        number = graphene.String(required=True)
        id = graphene.ID()
    carowner = graphene.Field(CarownerType)

    @classmethod
    def mutate(cls, root, info, number, id):
        carowner = Carowner.objects.get(pk=id)
        carowner.phone_number = number
        carowner.save()
        return UpdateCarownernumber(carowner=carowner)


class ParkingplaceInput(graphene.InputObjectType):
    placenumber = graphene.String()
    car_registrynumber = graphene.String()
    dateofpurchase = graphene.Date()


class CreateParkingplace(graphene.Mutation):
    class Arguments:
        input = ParkingplaceInput(required=True)

    parkingplace = graphene.Field(ParkingplacesType)

    @classmethod
    def mutate(cls, root, info, input):
        parkingplace = Parkingplaces()
        parkingplace.placenumber = input.placenumber
        parkingplace.dateofpurchase = input.dateofpurchase
        parkingplace.car_registrynumber = input.car_registrynumber
        parkingplace.save()
        return CreateParkingplace(parkingplace=parkingplace)




class Mutation(graphene.ObjectType):
    update_car = UpdateCar.Field()
    create_car = CreateCar.Field()
    create_carowner = CreateCarowner.Field()
    create_parkingplace = CreateParkingplace.Field()
    update_carownernumber = UpdateCarownernumber.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)