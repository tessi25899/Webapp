from django.urls import path
from .views import *

app_name = 'knowledges'

urlpatterns = [
    path('Wissensdatenbank/',index, name='index'),
    path('Wissensdatenbank/<str:slug>/',index_knowledge,name='detail'),
    path('Wissensdatenbank/<str:slug>/',KnowledgeDetailView,name='detail_content')
]
