from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import EventForm, EventForm


def index(request):
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    return render(request, template_name="events/index.html",context=context)

def show(request, unit):
    if unit == 'Alle':
        unitid = Unit.objects.all()
        context = {'events':Event.objects.filter().order_by('date'), 'units':Unit.objects.all(),}
    else:
        unitid = Unit.objects.get(slug=unit)
        context = {'events':Event.objects.filter(unit=unitid).order_by('date'), 'units':Unit.objects.all()}
    return render(request, template_name="events/index.html",context=context)

def event_create(request):
    context = {'events':Event.objects.filter().order_by('date'), 'units':Unit.objects.all(),'kinds':Kindtable.objects.all(),'titel':'Termin erstellen'}
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return render(request, template_name="events/index.html",context=context)
    else:
        form = EventForm()
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all(),'form':form, 'titel':'Termin bearbeiten'}
    return render(request, 'events/form.html', context=context )

def delete(request,pk):
    try:
        Event.objects.get(pk=pk).delete()
    
    finally:
        context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
        return render(request, template_name="events/index.html",context=context)

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all()}
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            print(event.date)
            event = form.save(commit=False)
            event.save()
            return render(request, template_name="events/index.html",context=context)
        else:
            print("not valid")
    else:
        form = EventForm(instance=event)
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all(),'form':form, 'titel':'Termin bearbeiten'}
    return render(request, 'events/form.html', context=context )