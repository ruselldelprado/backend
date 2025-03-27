from django.shortcuts import render,redirect
from .models import Incident
from .forms import IncidentForm
from django.contrib.auth.decorators import login_required


def hero(request):
    return render(request, 'dispatch/hero.html')


@login_required(login_url='/members/login_user/')
def home(request):
    return render(request, 'dispatch/home.html')


@login_required(login_url='/members/login_user/')
def personel(request):
    return render(request, 'dispatch/personel.html')


@login_required(login_url='/members/login_user/')
def dispatcher_report(request):
    return render(request, 'dispatch/dispatcher_report.html')


@login_required(login_url='/members/login_user/')
def showView(request):
    obj = Incident.objects.all()
    template_name = 'dispatch/calls.html'
    context = {'calls': obj}
    return render(request, template_name, context)


@login_required(login_url='/members/login_user/')
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


@login_required(login_url='/members/login_user/')
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


@login_required(login_url='/members/login_user/')
def deleteView(request, id):
    obj = Incident.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('calls')
    template_name = 'dispatch/confirmation.html'
    context = {'calls': obj}
    return render(request, template_name, context)
