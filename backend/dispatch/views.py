from django.shortcuts import render,redirect
from .models import Incident
from .forms import IncidentForm

def hero(request):
    return render(request, 'dispatch/hero.html')

def home(request):
    return render(request, 'dispatch/home.html')

def personel(request):
    return render(request, 'dispatch/personel.html')


def dispatcher_report(request):
    return render(request, 'dispatch/dispatcher_report.html')

def showView(request):
    obj = Incident.objects.all()
    template_name = 'dispatch/calls.html'
    context = {'calls': obj}
    return render(request, template_name, context)

def callsFormView(request):
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calls')
    template_name = 'dispatch/calls_form.html'
    context = {'form': form}
    return render(request, template_name, context)

def updateView(request, id):
    obj = Incident.objects.get(id=id)
    form = IncidentForm(instance=obj)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('calls')
    template_name = 'dispatch/calls_form.html'
    context = {'form': form}
    return render(request, template_name, context)


def deleteView(request, id):
    obj = Incident.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('calls')
    template_name = 'dispatch/confirmation.html'
    context = {'calls': obj}
    return render(request, template_name, context)
