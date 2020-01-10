from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

def index(request):
    context = {'events':Event.objects.all(),'units':Unit.objects.all()}
    return render(request, template_name="events/index.html",context=context)