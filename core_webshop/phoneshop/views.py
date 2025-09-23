from django.shortcuts import render
from .models import Products

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {"products": products})

def cart(request):
    return render(request, 'cart.html')

def receipts(request):
    return render(request, 'receipts.html')

def login(request):
    return render(request, 'login.html')