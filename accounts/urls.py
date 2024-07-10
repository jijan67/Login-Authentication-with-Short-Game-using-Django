from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]
