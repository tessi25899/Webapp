from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='index'),
    path('Termine/Einheit/<str:unit>',show ,name='show_events'),
    path('Termine/create/', views.event_create, name='event_create'),
    path('Termine/<int:pk>/delete/',delete, name='event_delete'),
    path('Termine/<int:pk>/edit/', views.event_edit, name="event_edit"),
]
