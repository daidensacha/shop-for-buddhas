from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
        "stars": [1, 2, 3, 4, 5],
    }

    return render(request, 'products/products.html', context)
