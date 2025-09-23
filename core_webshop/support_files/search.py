from phoneshop.models import Products

def search_products(name):
    return Products.objects.filter(name__icontains=name)
