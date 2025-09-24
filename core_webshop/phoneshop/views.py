from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Cart, Shops, Users, Sales
from support_files.sorting import sort_product

@login_required(login_url='/')
def index(request):
    # Alap queryset - minden termék
    products = Products.objects.all()

    all_categories = Products.objects.values_list("category", flat=True).distinct()

    products, categories = sort_product(request, products)



    context = {
        'products': products,
        'categories': categories,
        'allCategory': all_categories
    }

    return render(request, 'index.html', context)

@login_required(login_url='/')
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url='/')
def receipts(request):
    receipts = Sales.objects.all()
    return render(request, 'receipts.html',{'receipts': receipts})

@login_required(login_url='/')
def product_detail(request, name):
    product = get_object_or_404(Products, name=name)
    shops = Shops.objects.all()

    return render(request, 'item_info.html', {
        'product': product,
        'shops': shops
    })

@login_required
def user_cart(request):
    phoneshop_user = request.user.phoneshop_user
    cart_items = Cart.objects.filter(user_id=phoneshop_user.id)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    phoneshop_user = request.user.phoneshop_user
    print("Adding to cart for:", phoneshop_user.id)
    product = get_object_or_404(Products, id=product_id)

    shop_id = request.GET.get('shop')
    if not shop_id or not shop_id.isdigit():
        return HttpResponseBadRequest("Missing or invalid shop ID.")

    shop = get_object_or_404(Shops, id=shop_id)

    Cart.objects.create(
        user=phoneshop_user,
        product=product,
        shop=shop,
        quantity=1,
        price=product.price,
        color='black',
        storage=256
    )
    return redirect('user_cart')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Hibás felhasználónév vagy jelszó!'})
    return render(request, 'login.html')
