from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, oun_product, products_list


app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products'),
    # path('home/', home, name='home'),
    # path('contacts/', contacts, name='contacts')
    path('products/<int:pk>/', oun_product, name='oun_product')
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

