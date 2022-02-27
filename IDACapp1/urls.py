from IDACapp1 import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
     path('', views.index,name = 'home' ),
     path('explore', views.explore, name='explore'),
     path('about', views.about, name='about'),
     path('contact', views.contact, name='contact'),
     path('signin', views.signin, name='signin'),
     path('login', views.login, name='login'),
 ]
 
 