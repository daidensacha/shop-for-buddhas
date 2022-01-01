from django.shortcuts import render, redirect, get_object_or_404, \
                             HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db.models import F

from .models import UserProfile
# from .models import UserProfile, Favorite
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product
# import products.views


@login_required
def profile(request):

    if request.user.is_authenticated:

        """ Display the users profile """
        profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request,
                               'Update failed. Please ensure \
                                   the form is valid.')
        else:
            form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

        """ Products context to display the list of vendor products """
        try:
            products = Product.objects.filter(created_by=request.user)
        except Exception as e:
            messages.error(request, "No vendor proucts found.")
            products = None

        """ Vendor context create list of vendor sales """
        try:
            vendor_sales = OrderLineItem.objects.filter(
                                vendor__username=request.user.username)
        except Exception as e:
            messages.error(request, "No vendor sales found.")
            vendor_sales = None
        # Start with an empty favorites list
        favorite_list = []
        """Filter products for items associated with the authenticated user"""
        # Exclude items not selected. Order the list by category, name
        favorite_list = Product.objects.exclude(
                            favorites=None).filter(
                                favorites__username=request.user).order_by(
                                    'category', 'name')
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
            'favorite_list': favorite_list,
        }

        return render(request, template, context)
    else:
        messages.info(request, 'Please log in to add items to favorites.')
        return redirect('account_login')


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


def add_remove_favorite(request, product_id):
    """
    A function to add/ remove items to/ from users favorite list
    If user is authenticated add/ remove item to the favorites list
    else redirect user to the login page
    """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)

        # I in users favorite list delete it from the list
        if product.favorites.filter(id=request.user.id).exists():
            product.favorites.remove(request.user)
            messages.success(
                request, f'Removed {product.name} from favorites.')
        else:
            # Add the item to the users favorites list
            product.favorites.add(request.user)
            messages.success(request, f'Added {product.name} to favorites.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    else:
        messages.info(request, 'Please log in to add items to favorites.')
        return redirect('account_login')


def disable_account(request):
    """
    Function to disable user account
    """
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, f'The account for {user.first_name} \
                               {user.last_name} has been closed.')
    return redirect("account_logout")
