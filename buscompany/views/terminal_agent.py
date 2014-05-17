from django.shortcuts import render

def dashboard(request):
    return render(request, 'terminal_agent/dashboard.html')
