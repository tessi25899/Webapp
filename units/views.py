from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from datetime import datetime 
from .forms import UnitCreateForm
from webapp.utils import *



def index(request):
    a_user = check_admin(request.user)
    e_user = check_einheitsfueher(request.user)
    user_permissions = {'a_user':a_user, 'e_user':e_user}

    context = {'units':Unit.objects.exclude(slug="Stadt"),'user_permissions':user_permissions}
    return render(request, template_name="units/unit_index.html",context=context)

def detail(request, unit):
   # a_user = check_admin(request.user)
   # e_user = check_einheitsfueher(request.user)
    #user_permissions = {'a_user':a_user, 'e_user':e_user}

    context = {'units':Unit.objects.exclude(slug="Stadt")}#,'user_permissions':user_permissions}
    return render(request, template_name="units/unit_index.html",context=context)
