from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.categories, name='categories'),
    path('resources/', views.resources, name='resources'),

    path('contact/', views.contact, name='contact'),

    
]
