from django.shortcuts import render
from .models import Products
from support_files.sorting import sort_product

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

def cart(request):
    return render(request, 'cart.html')

def receipts(request):
    return render(request, 'receipts.html')

def login(request):
    return render(request, 'login.html')