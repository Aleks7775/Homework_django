from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def oun_product(request, pk):
    """Контролер одного товара"""
    prod = Product.objects.get(pk=pk)
    context = {"prod": prod}
    return render(request, 'oun_product.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {"product": products}
    return render(request, 'product_list.html', context)

