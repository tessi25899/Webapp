from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'events'

urlpatterns = [
    path('Termine/', index, name='index'),
    
    path('Termine/Einheit/<str:unit>',show ,name='show_events'),
    path('Termine/create/',create, name='create_events'),
    path('Termine/add/',add, name='add_events'),
    path('Termine/<int:pk>/edit/',edit, name='edit_events'),
    path('Termine/<int:id>/delete/',delete, name='delete_events'),
    
    #path('Termine/', index, name='event_index'),
    #path('Termine/Einheit/<str:unit>',show ,name='event_show'),
    #path('Termine/new/', views.event_new, name="event_new"),
    path('Termine/<int:pk>/edit', views.event_edit, name="event_edit"),
]
