from IDACapp1 import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
     path('', views.index,name = 'home' ),
     path('explore', views.explore, name='explore'),
 ]
 