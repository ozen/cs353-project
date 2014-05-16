from django.shortcuts import render

def dashboard(request):
    return render(request, 'manager_dashboard.html')
