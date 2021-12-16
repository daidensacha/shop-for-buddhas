from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product


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

    # products context
    try:
        products = Product.objects.filter(created_by=request.user)
    # Linting error, do not use bare except - fix
    except Exception as e:
        messages.error(request, "You dont have any products")
        products = None

    # vendor orders

    try:
        vendor_sales = OrderLineItem.objects.filter(vendor__username=request.user.username)
    # Linting error, do not use bare except - fix
    except Exception as e:
        messages.error(request, "You dont have any products")
        vendor_sales = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance= profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()
            messages.success(request, 'Profile updated successfully')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'products': products,
        'on_profile_page': True,
        'vendor_sales': vendor_sales,
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
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation of vendor sale for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def UserProfileUpdate(request):
    profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()

    context = {
        'form': form,
    }
    return redirect(request, "profiles/profile.html", context)