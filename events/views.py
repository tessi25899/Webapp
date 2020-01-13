from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import EventForm


def index(request):
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    return render(request, template_name="events/index.html",context=context)

def show(request, unit):
    if unit == 'alle':
        unitid = Unit.objects.all()
        context = {'events':Event.objects.filter().order_by('date'), 'units':Unit.objects.all(),}
    else:
        unitid = Unit.objects.get(slug=unit)
        context = {'events':Event.objects.filter(unit=unitid).order_by('date'), 'units':Unit.objects.all(),}
    return render(request, template_name="events/index.html",context=context)

def add(request):
    context = {'events':Event.objects.filter().order_by('date'), 'units':Unit.objects.all(),'kinds':Kindtable.objects.all(),}
    return render(request,'events/add.html',context=context)

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return render(request, 'events/index.html')
    return render(request, 'events/index.html')

def edit(request, id):
    if request.method == 'GET':
        form = EventForm(request.GET)
        
    #context = {'events':Event.objects.get(id=id), 'units':Unit.objects.all(),'kinds':Kindtable.objects.all(),}
    return render(request,'events/add.html')#,context=context)

def delete(request,id):
    try:
        Event.objects.get(id=id).delete()
    
    finally:
        context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    #return redirect(request, template_name="events/index.html",context=context)
        return render(request, template_name="events/index.html",context=context)