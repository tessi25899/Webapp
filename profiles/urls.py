from django.urls import include, re_path, path
from .views import *
from . import views


app_name = 'profiles'

urlpatterns = [
    path('Profil/', index, name='index'),
    path('Profil/<str:user>',detail ,name='detail_profil'),
]
