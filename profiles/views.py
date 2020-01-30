from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from units.models import Unit
from datetime import datetime 
from django.contrib.auth import get_user_model


def index(request):
    context = {'users': Profile.objects.all()}
    return render(request, template_name="profiles/index.html",context=context)

def detail(request, user):
    User = get_user_model()
    userid = User.objects.get(username=user)
    profileuser = Profile.objects.get(username=userid)
    context = {'profile': profileuser,'unit':Unit.objects.get(slug=profileuser.unit),'badges':ProfileBadges.objects.filter(user=profileuser),'hobbys':Hobby.objects.all()}
    return render(request, template_name="profiles/detail.html",context=context)