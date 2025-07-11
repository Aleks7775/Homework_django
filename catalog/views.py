from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category
import logging


class ProductListView(ListView):
    model = Product



class OunProductView(DetailView):
    model = Product

    #catalog/product_list.htm


# class ContactsView(TemplateView):
#     template_name = 'catalog/contacts.html'


# def home(request):
#     return render(request, 'home.html')
#
#
# def contacts(request):
#     return render(request, 'contacts.html')
#
#
# def oun_product(request, pk):
#     """Контролер одного товара"""
#     prod = get_object_or_404(Product, pk=pk)
#     context = {"prod": prod}
#     return render(request, 'product_detail.html', context)
#
#
# def products_list(request):
#     """Контролер главная"""
#     product = Product.objects.all()
#     context = {"product": product}
#     return render(request, 'product_list.html', context)



