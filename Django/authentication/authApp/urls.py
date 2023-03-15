from django.contrib import admin
from django.urls import path
from authApp import urls
from . import views

urlpatterns = [
    path('login', views.loginView.as_view(), name='Login'),
    path('logout', views.logoutView.as_view(), name='Logout'),
    path('protected', views.protectedView.as_view(), name='Protected'),
]