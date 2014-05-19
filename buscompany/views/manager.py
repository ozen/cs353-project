from django.shortcuts import render
from buscompany.models import *
from buscompany.forms import *

def dashboard(request):
    voyages = Voyage.objects.order_by('departure_time')[:5]

    buses = Bus.objects.all()[:5]

    garages = Garage.objects.all()[:5]
    for garage in garages:
        garage.buscount = IsAt.objects.filter(city=garage.city, address=garage.address).count()

    rentals = Rent.objects.all()[:5]
    for rent in rentals:
        rent.customer = RentedBy.objects.filter(plate=rent.plate, start_time=rent.start_time).tck_no

    return render(request, 'manager/dashboard.html', {'voyages': voyages, 'buses': buses, 'garages': garages, 'rentals': rentals})

def addBus(request):
    form = BusForm()
    return render(request, 'manager/add.html', {'form': form, 'type': 'Bus'})

def addBusType(request):
    form = BusTypeForm()
    return render(request, 'manager/add.html', {'form': form, 'type': 'BusType'})

def addGarage(request):
    form = GarageForm()
    return render(request, 'manager/add.html', {'form': form, 'type': 'Garage'})

def addRoute(request):
    form = RouteForm()
    return render(request, 'manager/add.html', {'form': form, 'type': 'Route'})

def addVoyage(request):
    form = VoyageForm()
    return render(request, 'manager/add.html', {'form': form, 'type': 'Voyage'})

def listBus(request):
    buses = Bus.objects.all()
    return render(request, 'manager/listBus.html', {'buses': buses})

def listBusType(request):
    busTypes = BusType.objects.all()
    return render(request, 'manager/listBusType.html', {'busTypes': busTypes})

def listGarage(request):
    garages = Garage.objects.all()
    for garage in garages:
        garage.buscount = IsAt.objects.filter(city=garage.city, address=garage.address).count()

    return render(request, 'manager/listGarage.html', {'garages': garages})

def listRoute(request):
    routes = Route.objects.all()
    return render(request, 'manager/listRoute.html', {'routes': routes})

def listVoyage(request):
    voyages = Voyage.objects.all()
    return render(request, 'manager/listVoyage.html', {'voyages': voyages})

