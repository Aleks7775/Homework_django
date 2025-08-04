from catalog.models import Product
from config.settings import CACHE_ENABLE
from django.core.cache import cache


def get_product_from_cache():
    """Получает данные по продуктам из кэша
    если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_category_product(category_id):
    # category_id = category_id['category_id']
    return Product.objects.filter(category_id=category_id)
