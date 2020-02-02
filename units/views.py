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

    context = {'nav_units':Unit.objects.exclude(slug="Stadt"),'user_permissions':user_permissions}
    return render(request, template_name="units/unit_index.html",context=context)

def detail(request, unit):
    a_user = check_admin(request.user)
    e_user = check_einheitsfueher(request.user)
    user_permissions = {'a_user':a_user, 'e_user':e_user}

    nav_units = Unit.objects.exclude(slug="Stadt")
    unit = Unit.objects.get(slug=unit)
    leaderships = Profile.objects.all().filter(unit=unit.id,role=ROLE_EINHEITSFUEHRUNG)
    young_leaderships = Profile.objects.all().filter(unit=unit.id,role=ROLE_JUGENDWART)


    amount_active = Profile.objects.all().filter(unit=unit.id,group=GROUP_ACTIVE).count()
    
    amount_young = Profile.objects.all().filter(unit=unit.id,group=GROUP_JUGEND).count()
    print("Anzahl der Mitglieder=",amount_young)

    context = {'nav_units':nav_units,'unit':unit,'young_leaderships':young_leaderships,'leaderships':leaderships,'user_permissions':user_permissions}
    return render(request, template_name="units/unit_detail.html",context=context)