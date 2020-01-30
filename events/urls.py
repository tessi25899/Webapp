from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='events_index'),
    #EVENT:
    path('Termine/<str:unit>', views.events_show, name='events_show'),
    path('Termine/create/', views.event_create, name='event_create'),
    path('Termine/edit/<int:pk>/', views.event_edit, name="event_edit"),
    path('Termine/delete/<int:pk>/',views.event_delete, name='event_delete'),

    #KINDTABLE:
    path('Kategorie/', views.kind_show, name='kind_show'),
    path('Kategorie/create/', views.kind_create, name='kind_create'),
    path('Kategorie/edit/<int:pk>/', views.kind_edit, name="kind_edit"),
    path('Kategorie/delete/<int:pk>/',views.kind_delete, name='kind_delete'),
    
]
