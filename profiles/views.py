from django.shortcuts import render, redirect, get_object_or_404, \
                             HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product


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
            products = Product.objects.filter(
                created_by=request.user).order_by('category', 'name')
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


@login_required
def order_history(request, order_number):
    """
    Get the order details
    Check the authenticated user owns the order
    Stop users viewing orders that are not theirs
    """
    order = get_object_or_404(Order, order_number=order_number)
    # Ensure users cannot view other users order information
    if not request.user.username == order.user_profile.user.username:
        messages.warning(request, 'Users can only view their own order \
            information.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.info(request, (
            f'This is a past confirmation for order number {order_number}.'
            'A confirmation email was sent on the order date.'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def vendor_order_history(request, order_number):
    """ Create list of vendors product sales """
    order = get_object_or_404(Order, order_number=order_number)

    sale_total = 0
    delivery_total = 0
    grand_total = 0
    # Return and filter list of vendor sale line items and totals
    order_item = OrderLineItem.objects.filter(order=order)
    for item in order_item:
        if request.user == item.product.created_by:
            sale_total += item.lineitem_total

    grand_total = sale_total + delivery_total
    # Ensure users cannot view other vendors sale order information
    if grand_total == 0:
        messages.warning(
            request, 'You can only access your own sales information')
        return redirect(request.META.get('HTTP_REFERER', 'profile'))
    else:
        messages.info(request, (
         f'This is a past confirmation of vendor \
            sale for order number {order_number}.'
        ))

    template = 'checkout/checkout_vendor_sales.html'
    context = {
        'order': order,
        'sale_total': sale_total,
        'delivery_total': delivery_total,
        'grand_total': grand_total,
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

        # If in users favorite list delete it from the list
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
