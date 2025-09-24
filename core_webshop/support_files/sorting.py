from phoneshop.models import Products
from django.db.models import Q


def sort_product(request, products):

    name = request.GET.get('name')
    category = request.GET.get('category')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    if name:
        name = name.replace(" ", "").lower()
        products = [p for p in products if name in p.name.replace(" ", "").lower()]


    if category and category != "all":
        products = products.filter(category=category)


    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)


    categories = Products.objects.values_list('category', flat=True).distinct()

    return products, categories
