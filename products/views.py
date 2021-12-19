from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
# from profiles.views import profile
# from profiles.models import UserProfile
# from .forms import CreateProduct
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # favorites = Favorite.objects.all()
    # favorites = Favorite.objects.filter(user=request.user)
    # user = request.user
    favorite_list = []
    # prod = Product.objects.all()
    # This filters only the products with favorites but for all users
    # prod = Product.objects.exclude(favorites=None)
    prod = Product.objects.filter(favorites__username=request.user)
    favorite_list = Product.objects.filter(favorites__username=request.user)


    # print(prod)
    # for i in prod:
        # print(i.favorites)
        # favorite_list = i.favorites.all()
        # all_favorites = i.favorites.all()
        
        # print(all_favorites)
        # for item in all_favorites:
            # if item == request.user:
                # print(item)
                # favorite_list.append(item)
                # print(favorite_list)
                # print(item)


    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'stars': [1, 2, 3, 4, 5],
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'favorite_list': favorite_list,
        # 'user': user,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'stars': [1, 2, 3, 4, 5],
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    # Restrict view to is_vendor , is_admin, or superusers
    if not request.user.user_type == "is_vendor" \
       and not request.user.is_authenticated or \
       not request.user.user_type == "is_admin" \
       and not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                                     Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    # Restrict view to is_vendor or superusers
    # Restrict view to is_vendor , is_admin, or superusers
    if not request.user.user_type == "is_vendor" \
       and not request.user.is_authenticated or \
       not request.user.user_type == "is_admin" \
       and not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                                     Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    # Restrict view to is_vendor , is_admin, or superusers
    if not request.user.user_type == "is_vendor" \
       and not request.user.is_authenticated or \
       not request.user.user_type == "is_admin" \
       and not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
