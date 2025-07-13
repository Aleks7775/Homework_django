from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, OunProductView, HomeView, ContactsView


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', OunProductView.as_view(), name='product_detail')
]
