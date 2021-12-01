from django.shortcuts import render
from testimonials.models import Testimonial
# Create your views here.


def index(request):
    """ A view to return the index page """
    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        "testimonials": testimonials,
        "stars": [1, 2, 3, 4, 5],
    }
    return render(request, 'home/index.html', context)
