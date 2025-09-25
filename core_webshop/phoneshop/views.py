from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Cart, Shops, Users, Sales, Workers
from support_files.sorting import sort_product
from django.http import HttpResponse, JsonResponse
from support_files.register import RegistrationForm
from django.contrib import messages
from .forms import WorkerForm
from .models import Products, Cart, Shops, Users, Sales, Workers

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

@login_required
def edit_my_worker(request):
    ps_user = get_object_or_404(
        Users.objects.select_related("worker"),
        user=request.user
    )
    worker = ps_user.worker
    if request.method == "POST":
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request, "A dolgozó adatai frissítve lettek.")
            return redirect("worker_edit")
    else:
        form = WorkerForm(instance=worker)

    return render(request, "workers_edit.html", {"form": form, "worker": worker})


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
