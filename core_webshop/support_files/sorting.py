from phoneshop.models import Products


def sortName(order=1):
    if order == -1:
        return Products.objects.all().order_by('-name')
    return Products.objects.all().order_by('name')

def sortPrice(order=1):
    if order == -1:
        return Products.objects.order_by('-price')
    return Products.objects.order_by('price')

def sortCategory(order=1):
    if order == -1:
        return Products.objects.order_by('-category')
    return Products.objects.order_by('category')


