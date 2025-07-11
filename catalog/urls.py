from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, OunProductView              #home, contacts, oun_product, products_list


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    # path('home/', home, name='home'),
    # path('contacts/', contacts, name='contacts')
    path('products/<int:pk>/', OunProductView.as_view(), name='product_detail')
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

