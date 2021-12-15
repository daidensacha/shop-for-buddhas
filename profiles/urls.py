from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
urlpatterns = [
    path('', views.profile, name='profile'),
     path('order_history/<order_number>', views.order_history, name='order_history'),
    path("update_profile/", views.UserProfileUpdate, name="update_profile"),
    path("password_change_done/",PasswordChangeDoneView.as_view(template_name= "allauth/account/password_change_done.html"),name = "password_change_done"),
    path("password_change/",PasswordChangeView.as_view(template_name= "allauth/account/password_change.html"),name = "password_change"),

   
]
