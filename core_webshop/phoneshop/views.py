import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import TruncMinute
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from openpyxl import Workbook
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from support_files.availability import *


from .models import Products, Cart, Shops, Users, Sales, Workers, Specs, Orders
from django.db.models import Sum

from support_files.sorting import sort_product
from django.http import HttpResponse, JsonResponse
from support_files.register import RegistrationForm
from support_files.add_prod import ProductForm
from support_files.add_order import OrderForm
from support_files.modify_product_info import SpecsForm
from support_files.add_cart import increment_cart_item
from django.urls import reverse
from support_files.sell_prod_from_cart import CheckoutForm
from support_files.user_updater import UserUpdateForm
from datetime import date


@login_required(login_url='/')
def index(request):

    products = Products.objects.all()

    phoneshop_user = request.user.phoneshop_user
    id = phoneshop_user.worker_id
    request.session['shop'] = Workers.objects.get(id=id).shop.name

    all_categories = Products.objects.values_list("category", flat=True).distinct()

    products, categories, filters= sort_product(request, products)

    context = {
        'products': products,
        'categories': categories,
        'allCategory': all_categories,
        "filters": filters
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
def checkout(request):
    phoneshop_user = Users.objects.get(user=request.user)
    worker = phoneshop_user.worker

    cart_items = Cart.objects.filter(user=phoneshop_user)

    if not cart_items.exists():
        return redirect('user_cart')

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            for item in cart_items:
                if (item.product.category == "Telefon"):
                    item.product.available[list_index(item.product.id, item.color, item.storage)]  -= item.quantity
                else:
                    item.product.available[list_index_for_accessories(item.product.id, item.color)] -= item.quantity
                item.product.save()

                Sales.objects.create(
                    quantity=item.quantity,
                    selling_time=timezone.now(),
                    tax_number=form.cleaned_data['tax_number'],
                    zip_code=form.cleaned_data['zip_code'],
                    address=form.cleaned_data['address'],
                    costumer_name=form.cleaned_data['costumer_name'],
                    city=form.cleaned_data['city'],
                    price=item.price,
                    color=item.color,
                    storage=item.storage,
                    product=item.product,
                    shop=item.shop,
                    user=item.user
                )


            cart_items.delete()

            return redirect('receipts')
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'worker': worker
    })

@login_required(login_url='/')
@csrf_exempt
def delete_receipt(request, id):
    try:
        qs = Sales.objects.filter(id=id)
        deleted_count, _ = qs.delete()
        return JsonResponse({"success": True, 'deleted': deleted_count})
    except Exception as e:
        return JsonResponse({"success": False, 'error': str(e)}, status=500)


@login_required(login_url='/')
def receipts(request):

    grouped_sales = (
        Sales.objects
        .annotate(selling_date=TruncMinute('selling_time'))
        .values("id",'costumer_name', 'selling_date')
        .annotate(total_price=Sum('price'))
        .order_by('-selling_date')
    )
    return render(request, 'receipts.html', {'receipts': grouped_sales})


@login_required(login_url='/')
def product_detail(request, name):
    product = get_object_or_404(Products, name=name)
    specs = None
    if product.category != "Tartozék":
        specs = Specs.objects.filter(product=product).first()

    phoneshop_user = request.user.phoneshop_user
    worker = Workers.objects.get(id=phoneshop_user.worker_id)
    shops = worker.shop

    form = OrderForm(request.POST or None, product=product, specs=specs)
    user_worker = Users.objects.get(user=request.user).worker

    if request.method == "POST" and form.is_valid():

        order = form.save(commit=False)
        order.product = product
        if (order.product.category == "Tartozék"):
            order.storage = 0
        order.status = "feldolgozás_alatt"
        order.shop = user_worker.shop
        order.order_time = timezone.now()
        order.save()
        return redirect("home")

    return render(request, 'item_info.html', {
        'product': product,
        'shops': shops,
        'form': form
    })


@login_required(login_url='/')
def user_cart(request):
    if request.user.is_superuser:
        return redirect('home')
    phoneshop_user = get_object_or_404(Users, user=request.user)
    cart_items = Cart.objects.filter(user_id=phoneshop_user.id)
    return render(request, 'cart.html', {'cart_items': cart_items})


@login_required(login_url='/')
def add_to_cart(request, product_id):

    
    if request.user.is_superuser:
        return redirect('home')
    phoneshop_user = request.user.phoneshop_user
    print("Adding to cart for:", phoneshop_user.id)
    product = get_object_or_404(Products, id=product_id)

    color = request.GET.get('color')
    storage = request.GET.get('storage')

    if not color or color.strip().lower() not in [c.lower() for c in product.colors]:
        return HttpResponseBadRequest("Missing or invalid color selection.")
    if product.category == 'Telefon':
        if not storage or storage not in [s for s in product.specs.storage]:
            return HttpResponseBadRequest("Missing or invalid storage selection.")
    else:
        storage = None

    id = phoneshop_user.worker_id
    worker = Workers.objects.get(id=id)
    shop = get_object_or_404(Shops, id=worker.shop_id)

    
    is_in_cart = increment_cart_item(shop, worker, product, color, storage)

    if (is_in_cart == False):
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


@login_required(login_url='/')
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


@login_required(login_url='/')
def add_product(request):
    all_categories = Products.objects.values_list("category", flat=True).distinct()

    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            category = form.cleaned_data["category"]

            if Products.objects.filter(name=name, category=category).exists():
                messages.add_message(request, messages.ERROR, "Ez a termék már létezik!")
                return render(request, 'add_product.html', {
                    'form': form,
                    "categories": all_categories
                })

            product = form.save()
            if product.category == 'Telefon':
                return redirect('edit_specs', product_id=product.id)
            else:
                return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {
        'form': form,
        "categories": all_categories
    })


@login_required(login_url='/')
def edit_specs(request, product_id):
    if not request.user.is_superuser:
        return redirect('home')
    product = get_object_or_404(Products, id=product_id)
    specs, created = Specs.objects.get_or_create(product=product,
                                                 defaults={
                                                     "weight": 0,
                                                     "battery": 0,
                                                     "release_date": timezone.now(),
                                                 })

    if request.method == 'POST':
        form = SpecsForm(request.POST, instance=specs)
        if form.is_valid():
            form.save()
            available_count = len(specs.storage) * len(specs.product.colors)
            product.available =  [10] * available_count
            product.save()
            return redirect('home')
    else:
        form = SpecsForm(instance=specs)

    return render(request, 'edit_specs.html', {'form': form, 'product': product})

@login_required(login_url='/')
def list_orders(request):
    orders = Orders.objects.all()

    return render(request, "list_orders.html", {
        "orders": orders
    })

@login_required(login_url='/')
def update_order(request, order_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            status = data.get("status")
            order = Orders.objects.get(id=order_id)

            old_status = order.status
            new_status = data.get("status")

            if new_status in dict(Orders.status_choices):
                if (old_status == new_status):
                    return JsonResponse({"success": True})

                order.status = new_status
                if (order.status == "törölve"):
                    order.delete()
                else:
                
                
                    if (order.product.category == "Telefon"):
                        order.product.available[list_index(order.product.id, order.color, order.storage)]  += order.quantity
                        
                    else:
                        order.product.available[list_index_for_accessories(order.product.id, order.color)] += order.quantity
                    order.product.save()
                    order.save()

                return JsonResponse({"success": True, "redirect_url": reverse("home")})
        except Orders.DoesNotExist:
            return JsonResponse({"success": False, "error": "Order not found"}, status=404)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

@login_required(login_url='/')
def user_list(request):
    if not request.user.is_superuser:
        return redirect('home')
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


@login_required(login_url='/')
def update_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('home')
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                if value != '' and value is not None:
                    setattr(user, field, value)
            user.save()
            return redirect('user_list')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})


def export_report_excel(request):

    wb = Workbook()
    ws = wb.active
    ws.title = "Sales"

    today = date.today()
    shop = request.session.get('shop')

    ws.append(["Termék neve", "Szín", "Tárhely", "Mennyiség", "Ár"])

    sales = Sales.objects.all()
    for sale in sales:
        # print(shop)
        # print(f"{type(sale.shop.name)} - {type(shop)}")
        # print(f"{type(sale.selling_time.date())} - {type(today)}")
        if (shop == sale.shop.name and today == sale.selling_time.date()):
            is_TB = ""
            if (sale.product.category == "Telefon"):        
                is_TB = "TB"
                if (sale.storage > 1):
                    is_TB = "GB"
            if (sale.product.category == "Tartozék"):
                sale.storage = '-'
            ws.append([
                sale.product.name,
                sale.color,
                str(sale.storage) + is_TB,
                str(sale.quantity) + "db",
                str(sale.price) + "Ft",
            ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = f"report_{shop}_{today}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'


    wb.save(response)
    return response