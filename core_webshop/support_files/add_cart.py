from phoneshop.models import Cart


def increment_cart_item(shop, worker_obj, p_name, color, storage):
    cart_items = Cart.objects.all()
    for item in cart_items:
        if (storage != None):
            storage = int(storage)
        name = item.user.worker
        if (item.shop == shop and name == worker_obj and item.product == p_name and item.color == color and item.storage == storage):
            item.quantity += 1
            item.price += item.product.price
            item.save()
            return True
    return False