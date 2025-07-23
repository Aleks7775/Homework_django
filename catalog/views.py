from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Product
from catalog.forms import ProductForm


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ProductListView(ListView):
    model = Product


class OunProductView(DetailView):
    model = Product


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
