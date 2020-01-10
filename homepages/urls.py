from django.urls import path
from .views import *

app_name = 'homepages'

urlpatterns = [
    path('',index, name='home'),
]
