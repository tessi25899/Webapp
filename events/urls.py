from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='index'),
    path('Termine/<str:unit>',show ,name='show_events'),
    path('Termine/create',create, name='create_events'),
]
