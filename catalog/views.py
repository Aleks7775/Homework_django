from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category
import logging


class ProductListView(ListView):
    model = Product


class OunProductView(DetailView):
    model = Product


def home(request):
    return render(request, 'catalog/home.html')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

