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

def addTerminal(request, pk):
    terminal = None
    if pk:
        try:
            terminal = Terminal.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Terminal could not found: '+ pk, 'redirect': '/manager/listTerminal'})

    if request.method == 'POST':
        form = TerminalForm(request.POST, instance=terminal) if terminal else TerminalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'Terminal saved.', 'redirect': '/manager/listTerminal'})
    else:
        form = TerminalForm(instance=terminal) if terminal else TerminalForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'Terminal'})

def addSalesOffice(request, pk):
    salesOffice = None
    if pk:
        try:
            salesOffice = SalesOffice.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'SalesOffice could not found: '+ pk, 'redirect': '/manager/listSalesOffice'})

    if request.method == 'POST':
        form = SalesOfficeForm(request.POST, instance=salesOffice) if salesOffice else SalesOfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/notification.html', {'message': 'SalesOffice saved.', 'redirect': '/manager/listSalesOffice'})
    else:
        form = SalesOfficeForm(instance=salesOffice) if salesOffice else SalesOfficeForm()

    return render(request, 'manager/add.html', {'form': form, 'type': 'SalesOffice'})

def addSalesperson(request, pk):
    salesperson = None
    staff = None
    if pk:
        try:
            salesperson = Salesperson.objects.get(pk=pk)
            staff = Staff.objects.get(tck_no=salesperson.tck_no)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'Salesperson could not found: '+ pk, 'redirect': '/manager/listSalesperson'})

    if request.method == 'POST':
        form = SalespersonForm(request.POST, instance=staff) if staff else SalespersonForm(request.POST)
        if form.is_valid():
            newStaff = form.save()
            newSalesperson = Salesperson(tck_no=newStaff, office_id=form.cleaned_data['office_id'], tickets_sold=form.cleaned_data['tickets_sold'])
            newSalesperson.save()
            return render(request, 'common/notification.html', {'message': 'Salesperson saved.' , 'redirect': '/manager/listSalesperson'})
    else:
        form = SalespersonForm(instance=staff) if staff else SalespersonForm()
        if salesperson:
            form.fields['office_id'].initial = salesperson.office_id
            form.fields['tickets_sold'].initial = salesperson.tickets_sold

    return render(request, 'manager/add.html', {'form': form, 'type': 'Salesperson'})

def addTerminalAgent(request, pk):
    terminalAgent = None
    staff = None
    if pk:
        try:
            terminalAgent = TerminalAgent.objects.get(pk=pk)
            staff = Staff.objects.get(tck_no=terminalAgent.tck_no)
        except ObjectDoesNotExist:
            return render(request, 'common/notification.html', {'message': 'TerminalAgent could not found: '+ pk, 'redirect': '/manager/listTerminalAgent'})

    if request.method == 'POST':
        form = TerminalAgentForm(request.POST, instance=staff) if staff else TerminalAgentForm(request.POST)
        if form.is_valid():
            newStaff = form.save()
            newTerminalAgent = TerminalAgent(tck_no=newStaff, terminal_id=form.cleaned_data['terminal_id'])
            newTerminalAgent.save()
            return render(request, 'common/notification.html', {'message': 'TerminalAgent saved.', 'redirect': '/manager/listTerminalAgent'})
    else:
        form = TerminalAgentForm(instance=staff) if terminalAgent else TerminalAgentForm()
        if terminalAgent:
            form.fields['terminal_id'].initial = terminalAgent.terminal_id

    return render(request, 'manager/add.html', {'form': form, 'type': 'TerminalAgent'})

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

def listTerminal(request):
    terminals = Terminal.objects.all()
    return render(request, 'manager/listTerminal.html', {'terminals': terminals})

def listSalesOffice(request):
    salesOffices = SalesOffice.objects.all()
    return render(request, 'manager/listSalesOffice.html', {'salesOffices': salesOffices})

def listSalesperson(request):
    salespeople = Salesperson.objects.all()
    return render(request, 'manager/listSalesperson.html', {'salespeople': salespeople})

def listTerminalAgent(request):
    terminalAgents = TerminalAgent.objects.all()
    return render(request, 'manager/listTerminalAgent.html', {'terminalAgents': terminalAgents})

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

def deleteTerminal(request, pk):
    try:
        terminal = Terminal.objects.get(pk=pk)
        terminal.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Terminal could not found: '+ pk, 'redirect': '/manager/listTerminal'})
    return render(request, 'common/notification.html', {'message': 'Terminal deleted.', 'redirect': '/manager/listTerminal'})

def deleteSalesOffice(request, pk):
    try:
        salesOffice = SalesOffice.objects.get(pk=pk)
        salesOffice.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'SalesOffice could not found: '+ pk, 'redirect': '/manager/listSalesOffice'})
    return render(request, 'common/notification.html', {'message': 'SalesOffice deleted.', 'redirect': '/manager/listSalesOffice'})

def deleteSalesperson(request, pk):
    try:
        salesperson = Staff.objects.get(pk=pk)
        salesperson.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'Salesperson could not found: '+ pk, 'redirect': '/manager/listSalesperson'})
    return render(request, 'common/notification.html', {'message': 'Salesperson deleted.', 'redirect': '/manager/listSalesperson'})

def deleteTerminalAgent(request, pk):
    try:
        terminalAgent = Staff.objects.get(pk=pk)
        terminalAgent.delete()
    except ObjectDoesNotExist:
        return render(request, 'common/notification.html', {'message': 'TerminalAgent could not found: '+ pk, 'redirect': '/manager/listTerminalAgent'})
    return render(request, 'common/notification.html', {'message': 'TerminalAgent deleted.', 'redirect': '/manager/listTerminalAgent'})

