from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('lesson', views.lesson, name="lesson"), 
    path('fact', views.fact, name="fact"), 
    path('quizes', views.quizes, name="quizes"), 
    path('login', views.login_view, name="login"), 
    path('register', views.register_view, name="register"), 
    path('contact', views.contact, name="contact"), 
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),

          path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='quiz/forgot-password.html',
            email_template_name='quiz/password_reset_email.html',
            subject_template_name='quiz/password_reset_subject.txt',
            success_url='/forgot-password/done/'
        ),
        name='password_reset'
    ),

    # Email sent page
    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='quiz/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Link from email (enter new password)
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='quiz/password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),

    # Success page
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='quiz/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]