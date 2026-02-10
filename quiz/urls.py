from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('lesson', views.lesson, name="lesson"), 
    path('fact', views.fact, name="fact"), 
    path('quizes', views.quizes, name="quizes"), 
    path('login', views.login, name="login"), 
    path('register', views.register, name="register"), 
    path('forgot-password', views.forgotPassword, name="forgot-pswd"), 
]