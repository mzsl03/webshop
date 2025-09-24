from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import Products
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
    return render(request, 'receipts.html')


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
