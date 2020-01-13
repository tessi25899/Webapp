from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='index'),
    path('Termine/Einheit/<str:unit>',show ,name='show_events'),
    path('Termine/create/',create, name='create_events'),
    path('Termine/add/',add, name='add_events'),
    path('Termine/edit/<int:id>',edit, name='edit_events'),
    path('Termine/delete/<int:id>',delete, name='delete_events'),
]
