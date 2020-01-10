from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

def index(request):
    context = {'news':News.objects.all()}
    return render(request=request, template_name='homepages/index.html',context=context)

