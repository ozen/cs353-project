from django.shortcuts import render
from buscompany.models import *
from buscompany.forms import *
from django.core.exceptions import ObjectDoesNotExist

def dashboard(request):
    voyages = Voyage.objects.order_by('departure_time')[:5]

    buses = Bus.objects.all()[:5]

    garages = Garage.objects.all()[:5]
    for garage in garages:
        garage.buscount = IsAt.objects.filter(pk=garage.pk).count()

    rentals = Rent.objects.all()[:5]
    for rent in rentals:
        rent.customer = RentedBy.objects.filter(plate=rent.plate, start_time=rent.start_time).tck_no

    return render(request, 'manager/dashboard.html', {'voyages': voyages, 'buses': buses, 'garages': garages, 'rentals': rentals})

def addBus(request, plate):
    bus = None
    if plate:
        try:
            bus = Bus.objects.get(plate=plate)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Bus could not found: '+ plate, 'redirect': '/manager/listBus'})

    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus) if bus else BusForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Bus saved.', 'redirect': '/manager/listBus'})
    else:
        form = BusForm(instance=bus) if bus else BusForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'Bus'})

def addBusType(request, pk):
    busType = None
    if pk:
        try:
            busType = BusType.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Bus type could not found: '+ pk, 'redirect': '/manager/listBusType'})

    if request.method == 'POST':
        form = BusTypeForm(request.POST, instance=busType) if busType else BusForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Bus type saved.', 'redirect': '/manager/listBusType'})
    else:
        form = BusTypeForm(instance=busType) if busType else BusTypeForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'BusType'})

def addGarage(request, pk):
    garage = None
    if pk:
        try:
            garage = Garage.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Garage could not found: '+ pk, 'redirect': '/manager/listGarage'})

    if request.method == 'POST':
        form = GarageForm(request.POST, instance=garage) if garage else GarageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Garage saved.', 'redirect': '/manager/listGarage'})
    else:
        form = GarageForm(instance=garage) if garage else GarageForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'Garage'})

def addRoute(request, pk):
    route = None
    if pk:
        try:
            route = Route.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Route could not found: '+ pk, 'redirect': '/manager/listRoute'})

    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route) if route else RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Route saved.', 'redirect': '/manager/listRoute'})
    else:
        form = RouteForm(instance=route) if route else RouteForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'Route'})

def addVoyage(request, pk):
    voyage = None
    if pk:
        try:
            voyage = Voyage.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Voyage could not found: '+ pk, 'redirect': '/manager/listVoyage'})

    if request.method == 'POST':
        form = VoyageForm(request.POST, instance=voyage) if voyage else VoyageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Voyage saved.', 'redirect': '/manager/listVoyage'})
    else:
        form = VoyageForm(instance=voyage) if voyage else VoyageForm()

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
        garage.buscount = IsAt.objects.filter(pk=garage.pk).count()

    return render(request, 'manager/listGarage.html', {'garages': garages})

def listRoute(request):
    routes = Route.objects.all()
    return render(request, 'manager/listRoute.html', {'routes': routes})

def listVoyage(request):
    voyages = Voyage.objects.all()
    return render(request, 'manager/listVoyage.html', {'voyages': voyages})

def deleteBus(request, plate):
    try:
        bus = Bus.objects.get(plate=plate)
        bus.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Bus could not found: '+ plate, 'redirect': '/manager/listBus'})
    return render(request, 'common/notification.html', {'message': 'Bus deleted.', 'redirect': '/manager/listBus'})

def deleteBusType(request, pk):
    try:
        busType = BusType.objects.get(pk=pk)
        busType.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Bus type could not found: '+ pk, 'redirect': '/manager/listBusType'})
    return render(request, 'common/notification.html', {'message': 'Bus type deleted.', 'redirect': '/manager/listBusType'})

def deleteGarage(request, pk):
    try:
        garage = Garage.objects.get(pk=pk)
        garage.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Garage could not found: '+ pk, 'redirect': '/manager/listGarage'})
    return render(request, 'common/notification.html', {'message': 'Garage deleted.', 'redirect': '/manager/listGarage'})

def deleteRoute(request, pk):
    try:
        route = Route.objects.get(pk=pk)
        route.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Route could not found: '+ pk, 'redirect': '/manager/listRoute'})
    return render(request, 'common/notification.html', {'message': 'Route deleted.', 'redirect': '/manager/listRoute'})

def deleteVoyage(request, pk):
    try:
        voyage = Voyage.objects.get(pk=pk)
        voyage.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Voyage could not found: '+ pk, 'redirect': '/manager/listVoyage'})
    return render(request, 'common/notification.html', {'message': 'Voyage deleted.', 'redirect': '/manager/listVoyage'})

