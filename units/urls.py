from django.urls import path
from .views import *
from . import views

app_name = 'units'

urlpatterns = [
    path('Standorte/', index, name='units_index'),
    path('Standorte/<str:unit>', detail, name='unit_detail'),
    #path('Standorte/create',create_unit, name='create_unit'),
   # path('',detail_unit,name="detail_unit"),
]
