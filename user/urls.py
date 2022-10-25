from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='experience'),
    path('index/', views.index, name='education'),
    path('index/', views.index, name='skill'),
    path('index/', views.index, name='blog'),
    
    path('index/', views.index, name='message'),
    path('index/', views.index, name='activity'),
    path('index/', views.index, name='portfolio'),
    
  
]
