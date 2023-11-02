from django.urls import path
from productos.views import productos, altaProductos

urlpatterns = [
        path('', productos, name="productos"),
        path('altaProductos/', altaProductos, name="altaProductos"),
]