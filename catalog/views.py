from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from catalog.models import Product
from catalog.forms import ProductForm


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")
        product.is_published = False
        product.save()

        return redirect('catalog:product_list')


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

    def delete(self, request, *args, **kwargs):
        product = self.get_object()

        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        return super().delete(request, *args, **kwargs)

