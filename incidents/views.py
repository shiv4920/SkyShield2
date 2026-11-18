from django.shortcuts import render, redirect
from .models import Incident

def dashboard(request):
    incidents = Incident.objects.all().order_by('-reported_date')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        severity = request.POST.get('severity')
        if title and description:
            Incident.objects.create(title=title, description=description, severity=severity)
            return redirect('dashboard')
    return render(request, 'incidents/dashboard.html', {'incidents': incidents})
