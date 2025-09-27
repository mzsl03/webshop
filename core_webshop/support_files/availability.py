from django.core.exceptions import ObjectDoesNotExist
from phoneshop.models import Products, Specs

def list_index(product_id, szin, tarhely) :
    try:
        product = Products.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise ValueError(f"A termék azonosítóval ({product_id}) nem található.")

    szin_lista = [x for x in product.colors]

    try:
        index_szin = szin_lista.index(szin)
    except ValueError:
        raise ValueError(f"A szín '{szin}' nem található a termékhez.")

    try:
        specs = Specs.objects.get(product_id=product_id)
    except ObjectDoesNotExist:
        raise ValueError(f"A termékhez ({product_id}) nem található specifikáció.")

    tarhely_lista = [int(x) for x in specs.storage]

    try:
        index_tarhely = [int(x) for x in tarhely_lista].index(tarhely)
    except ValueError:
        raise ValueError(f"A tárolókapacitás '{tarhely}' nem található a termékhez.")

    result = (index_tarhely * len(szin_lista)) + index_szin
    return result


def list_index_for_accessories(product_id, szin) :
    try:
        product = Products.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise ValueError(f"A termék azonosítóval ({product_id}) nem található.")

    szin_lista = [x for x in product.colors]

    try:
        index_szin = szin_lista.index(szin)
    except ValueError:
        raise ValueError(f"A szín '{szin}' nem található a termékhez.")

    return index_szin
