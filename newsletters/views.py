from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import NewsForm

def index(request):
    model = [News]
    context = {'newsletters':News.objects.all()}
    return render(request, template_name="newsletters/index.html",context=context)

def create(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            newmessage = form.save(commit=False)
            newmessage.created_by = request.user
            newmessage.save()
    return render(request, 'newsletters/index.html')
