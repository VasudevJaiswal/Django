
from django.contrib import admin
from django.urls import path
from home import views
from about import views

urlpatterns = [
    path("", views.index,name='home'),
    path("", views.about,name ='about')
]
