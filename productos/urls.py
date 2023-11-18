from django.urls import path
from productos.views import productos, altaProductos, edicionProducto

urlpatterns = [
        path('', productos, name="productos"),
        path('altaProductos/', altaProductos, name="altaProductos"),
        path('edicionProducto/', edicionProducto, name="edicionProducto"),
]