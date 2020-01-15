from django.urls import path
from .views import *
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('News/', index, name='index_news'),
    path('News/create',create, name='create_news')
]
