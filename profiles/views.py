from django.shortcuts import render, redirect, get_object_or_404, \
                             HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
# from .models import UserProfile, Favorite
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product
# import products.views


@login_required
def profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # products context to display the list of vendor products
    try:
        products = Product.objects.filter(created_by=request.user)
    except Exception as e:
        messages.error(request, "No vendor proucts found.")
        products = None

    # vendor orders
    try:
        vendor_sales = OrderLineItem.objects.filter(vendor__username=request.user.username)
    except Exception as e:
        messages.error(request, "No vendor sales found.")
        vendor_sales = None

    favorite_list = []
    # favorite_list = Product.objects.filter(favorites__username=request.user)
    favorite_list = Product.objects.exclude(favorites=None).filter(favorites__username=request.user)

    all_products = Product.objects.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'products': products,
        'all_products': all_products,
        'on_profile_page': True,
        'vendor_sales': vendor_sales,
        "favorite_list": favorite_list,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def vendor_order_history(request, order_number):
    """ Create list of vendors product sales """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation of vendor \
            sale for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# @login_required
# def add_remove_favorite(request, product_id):
#     """ Add product to users favorites list """
#     if request.user.is_authenticated:
#         user = request.user
#         product = Product.objects.get(id=product_id)
#         try:
#             a = Favorite.objects.get(product__id=product_id)
#             a.delete()
#             messages.info(request, f'Removed {product.name} from favorites.')
#             # messages.info(request, "Product removed from favorites")
#             return redirect("products")
#         except:
#             # Favorite.objects.create(user=request.user, product=product_id)
#             Favorite.objects.create(user=user, product=product)
#             messages.info(request, f'Added {product.name} to favorites.')
#             # messages.info(request, "Product added to favorites")
#             return redirect("products")
#     else:
#         return redirect("login")

# @login_required
# def add_remove_favorite(request, product_id):
#     """ Add product to users favorites list """
#     if request.user.is_authenticated:
#         user = request.user
#         product = Product.objects.get(id=product_id)
#         favorite = Favorite.objects.filter(product__id=product_id)
#         # Check list for selected item amd delete if in list.
#         if favorite:
#             favorite.delete()
#             messages.info(request, f'Removed {product.name} from favorites.')
#             return redirect("products")
#         else:
#             # add item to favorites list
#             Favorite.objects.create(user=user, product=product)
#             messages.info(request, f'Added {product.name} to favorites.')
#             return redirect("products")
#     else:
#         return redirect("login")

@login_required
def add_remove_favorite(request, product_id):
    """ Add or remove user id  favorites list """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        """ 
        Check if the selected item is already in the users favorites
        and if it is, delete it from the list
        """
        if product.favorites.filter(id=request.user.id).exists():
            product.favorites.remove(request.user)
            messages.info(request, f'Removed {product.name} from favorites.')
        else:
            """ Add the item to the users list of favorites """
            product.favorites.add(request.user)
            messages.info(request, f'Added {product.name} to favorites.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@ login_required
def favorite_list(request):
    # new = Product.objects.filter(favorites=request.user.id)
    # favorite_list = Product.objects.filter(favorites=request.user.id)
    # user = request.user
    # products = Product.objects.all()
    # favorite_list = user.favorites.all()
    favorite_list = []
    prod = Product.objects.all()
    for i in prod:

        # favorite_list = i.favorites.all()
        all_favorites = i.favorites.all()
        
        print(favorite_list)
        for item in all_favorites:
            if item == request.user:
                favorite_list.append(item)
                print(favorite_list)
                # print(item)

    context = {
        # 'favorite_list': favorite_list,
        # 'products': products
    }
    # favorite_list = Product.favorites.filter(request.user.id)
    # favorite_list = Product.objects.all()
    print(favorite_list)
    return render(request, 'profile', context)

# Example https://github.com/veryacademy/YT-Django-Simple-Blog-App-Part10-User-Favourties-Save/blob/master/accounts/views.py
# @ login_required
# def favourite_list(request):
#     new = Post.newmanager.filter(favourites=request.user)
#     return render(request,
#                   'accounts/favourites.html',
#                   {'new': new})