from django.shortcuts import render

def dashboard(request):
    return render(request, 'agent_dashboard.html')
