from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404,
    HttpResponseRedirect
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to render that cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name}' +
            f' quantity to {cart[item_id]}', extra_tags='is_cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart',
                         extra_tags='is_cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of a specified product in the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} ' +
            f'quantity to {cart[item_id]}', extra_tags='is_cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart',
                         extra_tags='is_cart')

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)

        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart',
                         extra_tags='is_cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def coupon(request):
    """Return an error message for the coupon"""
    # This returns error for now untill functionality is added
    if request.method == 'POST':
        messages.warning(request, 'The coupon you entered is not valid!')
        path = request.POST['redirect']
        return redirect(path)
