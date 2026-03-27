from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('lesson', views.lesson, name="lesson"), 
    path('fact', views.fact, name="fact"), 
    path('quizes', views.quizes, name="quizes"),  
    path('contact', views.contact, name="contact")
]