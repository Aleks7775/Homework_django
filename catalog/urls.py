from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
