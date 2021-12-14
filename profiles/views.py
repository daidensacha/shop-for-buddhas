from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product
# Create your views here.


def profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    # Order context creation
    try:
        orders = Order.objects.filter(user_profile__user=request.user)
        print(orders)
    except:
        orders = None
   
     
    #products context
    try:
        products = Product.objects.filter(created_by = request.user)
    except:
        products = None

     # vendor orders
    vendor_order_list = []
    if products != None:
        for product in products:
            vendor_orders = OrderLineItem.objects.filter(product=product)
            vendor_order_list.append(vendor_orders)

    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        "form":form,
        "orders":orders,
        "products":products,
        "vendor_order_list":vendor_order_list,
    }

    return render(request, template, context)

def UserProfileUpdate(request):
    profile = UserProfile.objects.get(user= request.user)
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST,instance= profile)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.user = request.user
            update_form.save()

    context = {
        "form":form,
    }
    return redirect(request,"profiles/profile.html",context)