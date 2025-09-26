import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Products, Cart, Shops, Users, Sales, Workers
from support_files.sorting import sort_product
from django.http import HttpResponse, JsonResponse
from support_files.register import RegistrationForm
from support_files.add_prod import ProductForm


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
    if request.user.is_superuser:
        return redirect('home')
    return render(request, 'cart.html')

@require_POST
def delete_cart_item(request, item_id):
    if request.user.is_superuser:
        return redirect('home')
    try:
        item = Cart.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

@login_required(login_url='/')
def receipts(request, receipt_id=None):
    if request.method == "DELETE" and receipt_id:
        receipt_item = get_object_or_404(Sales, id=receipt_id)
        receipt_item.delete()
        return render(request, 'receipts.html', {
            'receipts': Sales.objects.all()
        })
    receipts = Sales.objects.all()
    return render(request, 'receipts.html', {'receipts': receipts})

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
    if request.user.is_superuser:
        return redirect('home')
    phoneshop_user = request.user.phoneshop_user
    cart_items = Cart.objects.filter(user_id=phoneshop_user.id)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    if request.user.is_superuser:
        return redirect('home')
    phoneshop_user = request.user.phoneshop_user
    print("Adding to cart for:", phoneshop_user.id)
    product = get_object_or_404(Products, id=product_id)

    shop_id = request.GET.get('shop')
    color = request.GET.get('color')
    storage = request.GET.get('storage')

    if not shop_id or not shop_id.isdigit():
        return HttpResponseBadRequest("Missing or invalid shop ID.")
    if not color or color.strip().lower() not in [productColor.lower() for productColor in product.colors]:
        return HttpResponseBadRequest("Missing or invalid color selection.")
    if not storage or storage not in [s for s in product.specs.storage]:
        return HttpResponseBadRequest("Missing or invalid storage selection.")

    shop = get_object_or_404(Shops, id=shop_id)

    Cart.objects.create(
        user=phoneshop_user,
        product=product,
        shop=shop,
        quantity=1,
        price=product.price,
        color=color,
        storage=storage
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

@login_required
def register(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():

            worker = Workers.objects.create(
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                address=form.cleaned_data['address'],
                birth_date=form.cleaned_data['birth_date'],
                phone_number=form.cleaned_data['phone_number'],
                position=form.cleaned_data['position'],
                shop=form.cleaned_data['shop'],
                admin=False
            )


            user = User.objects.create_user(
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )


            Users.objects.create(
                user=user,
                worker=worker
            )

            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'register_worker.html', {'form': form})

@login_required
def add_product(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
