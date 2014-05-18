from django.shortcuts import render
from buscompany.models import Voyage, Route, Bus, BusType

def dashboard(request):
    voyages = Voyage.objects.order_by('departure_time')[:5]
    return render(request, 'manager/dashboard.html', {'voyages': voyages})
