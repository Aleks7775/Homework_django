from django.shortcuts import render, get_object_or_404
from catalog.models import Product
import logging


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def oun_product(request, pk):
    """Контролер одного товара"""
    prod = get_object_or_404(Product, pk=pk)
    context = {"prod": prod}
    return render(request, 'oun_product.html', context)


def products_list(request):
    """Контролер главная"""
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'product_list.html', context)

