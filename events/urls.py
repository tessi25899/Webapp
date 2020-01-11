from django.urls import path
from .views import *
from . import views

app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='index'),
    path('Termine/create',create, name='create_events')
]
