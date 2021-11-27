from django.shortcuts import render
from testimonials.models import Testimonial
# Create your views here.


def index(request):
    """ A view to return the index page """
    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        "testimonials": testimonials
    }
    return render(request, 'home/index.html', context)
