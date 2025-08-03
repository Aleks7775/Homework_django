from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, OunProductView, HomeView, ContactsView,
                           ProductCreate, ProductUpdateView, ProductDeleteView, ProductCategoryListView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(OunProductView.as_view()), name='product_detail'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/category/<int:category_id>/', ProductCategoryListView.as_view(), name='product_category_list')
]
