from django.urls import path
from .views import *

app_name = 'documents'

urlpatterns = [
    path('Dokumentvorlagen',index, name='documents_index'),
]
