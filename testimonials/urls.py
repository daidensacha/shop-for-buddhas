from django.urls import path
from .views import testimonial_view
urlpatterns = [
    path('', testimonial_view, name='testimonial_view'),
]
