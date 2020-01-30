from django.urls import path
from .views import *
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('News/', index, name='news_index'),
    #News
    path('News/<str:topic>', views.news_show, name='news_show'),
    path('News/create/', views.news_create, name='news_create'),
    path('News/edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('News/delete/<int:pk>/',views.news_delete, name='news_delete'),
    #Topic
    path('Themen/', views.topic_show, name='topic_show'),
    path('Themen/create/', views.topic_create, name='topic_create'),
    path('Themen/edit/<int:pk>/', views.topic_edit, name="topic_edit"),
    path('Themen/delete/<int:pk>/',views.topic_delete, name='topic_delete'),
]
