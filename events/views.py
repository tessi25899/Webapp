from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import EventForm, KindForm


def index(request):
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    return render(request, template_name="events/event_index.html",context=context)

#EVENT:
def events_show(request, unit):
    if unit == 'Alle':
        unitid = Unit.objects.all()
        context = {'events':Event.objects.filter().order_by('date'), 'units':Unit.objects.all(),}
    else:
        unitid = Unit.objects.get(slug=unit)
        context = {'events':Event.objects.filter(unit=unitid).order_by('date'), 'units':Unit.objects.all()}
    return render(request, template_name="events/event_index.html",context=context)
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect(reverse('events:events_index'))
    else:
        form = EventForm()
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all(),'form':form, 'titel':'Termin erstellen'}
    return render(request, 'events/event_form.html', context=context )
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all()}
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect(reverse('events:events_index'))
    else:
        form = EventForm(instance=event)
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all(),'form':form, 'titel':'Termin bearbeiten'}
    return render(request, 'events/event_form.html', context=context )
def event_delete(request,pk):
    try:
        Event.objects.get(pk=pk).delete()
    
    finally:
        return redirect(reverse('events:events_index'))

#KINDTABLE
def kind_show(request):
    context = {'kinds':Kindtable.objects.all(), 'units':Unit.objects.all(),}
    return render(request, template_name="events/kind_index.html",context=context)
def kind_create(request):
    if request.method == "POST":
        form = KindForm(request.POST)
        if form.is_valid():
            kind = form.save(commit=False)
            kind.save()
            print("create")
            return redirect(reverse('events:kind_show'))
    else:
        form = KindForm()
    context = {'units':Unit.objects.all(), 'kinds':Kindtable.objects.all(),'form':form, 'titel':'Kategorie bearbeiten'}
    return render(request, 'events/kind_form.html', context=context )
def kind_edit(request, pk):
    event = get_object_or_404(Kindtable, pk=pk)
    if request.method == "POST":
        form = KindForm(request.POST, instance=event)
        if form.is_valid():
            kind = form.save(commit=False)
            kind.save()
            return redirect(reverse('events:kind_show'))
        else:
            print("not valid")
    else:
        form = KindForm(instance=event)
    context = {'units':Unit.objects.all(), 'form':form, 'titel':'Kategorie bearbeiten'}
    return render(request, 'events/kind_form.html', context=context )
def kind_delete(request,pk):
    try:
        Kindtable.objects.get(pk=pk).delete()
    finally:
        return redirect(reverse('events:kind_show'))

