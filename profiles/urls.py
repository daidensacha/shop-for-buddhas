from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib.auth.views import (PasswordChangeView,
#                                        PasswordChangeDoneView)
urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('vendor_order_history/<order_number>', views.vendor_order_history,
         name='vendor_order_history'),
    path('add_remove_favorite/<int:product_id>/', views.add_remove_favorite,
         name='add_remove_favorite'),
]
