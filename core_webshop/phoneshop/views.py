from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def receipts(request):
    return render(request, 'receipts.html')