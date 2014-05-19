from django.shortcuts import render
from buscompany.models import Voyage, Bus, Garage, Rent, IsAt, RentedBy
from buscompany.forms import BusForm

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
    return render(request, 'manager/add.html', {'form': form})
