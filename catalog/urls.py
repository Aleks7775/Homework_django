from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, OunProductView, HomeView, ContactsView,
                           ProductCreate, ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', OunProductView.as_view(), name='product_detail'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
