from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import UnitCreateForm

def index(request):
    model = [Unit,]
    context = {'units':Unit.objects.all()}
    return render(request, template_name="units/index.html",context=context)

def detail(request, slug):
    model = [Unit,]
    context = {'unit':Units.objects.all().filter(slug=slug)}
    return render(request, template_name="units/detail.html",context=context)

def create_unit(request):
    if request.method == "POST":
        form = UnitCreateForm(request.POST)
        print("form")
        try:
            if form.is_valid():
                print("ja")
                unit = form.save(commit=False)
                unit.save()
                print('save')
                return render(request, 'units/index.html')
        except Exception as e:
            print (e)
    return render(request, 'units/index.html')