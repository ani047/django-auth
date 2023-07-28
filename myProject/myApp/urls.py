
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("user_register",views.user_register,name='register'),
    path("user_login",views.user_login,name='user_login'),
    path('user_profile',views.user_profile,name='user_profile')
    
]