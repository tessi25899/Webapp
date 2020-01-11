from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import EventForm


def index(request):
    model = [Unit, Event]
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    return render(request, template_name="events/index.html",context=context)

def index_k(request):
    model = [Unit, Event]
    context = {'events':Event.objects.all().order_by('date'),'units':Unit.objects.all(), 'kinds':Kindtable.objects.all()}
    return render(request, template_name="events/index.html",context=context)

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return render(request, 'events/index.html')
    return render(request, 'events/index.html')
