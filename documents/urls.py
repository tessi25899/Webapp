from django.urls import path
from .views import *

app_name = 'documents'

urlpatterns = [
    path('Dokumentvorlagen',index, name='documents_index'),
    path('Dokumentvorlagen/<str:name>',detail, name='document_detail'),
    path('Dokumentvorlagen/create/document',document_create, name='document_create'),
    path('Dokumentvorlagen/delete/<int:pk>/',delete, name='document_delete'),
    path('Dokumentvorlagen/download/<int:id>/',document_download, name='document_download')
]
