from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden

from catalog.models import Product
from catalog.forms import ProductForm

import logging

from catalog.services import get_product_from_cache, get_category_product

logger = logging.getLogger(__name__)


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

    def get_queryset(self):
        return get_product_from_cache()


class OunProductView(DetailView):
    model = Product


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.change_product'):
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав для удаления продукта.")


class ProductCategoryListView(ListView):
    model = Product
    template_name = "catalog/product_category_list.html"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_category_product(category_id)


# class ProductDeleteView(LoginRequiredMixin, TemplateView):
"""Если потребуется более гибкая проверка прав"""
#     template_name = 'catalog/product_confirm_delete.html'
#
#     def post(self, request, **kwargs):
#         product = get_object_or_404(Product, id=kwargs['pk'])
#
#         if not request.user.has_perm('catalog.delete_product'):
#             return HttpResponseForbidden("У вас нет прав для удаления продукта.")
#
#         product.delete()
#
#         return redirect('catalog:product_list')
