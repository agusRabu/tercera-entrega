from django.urls import path
from productos.views import productos, altaProductos, edicionProducto, editarProducto, eliminarProducto

urlpatterns = [
        path('', productos, name="productos"),
        path('altaProductos/', altaProductos, name="altaProductos"),
        path('edicionProducto/<id>', edicionProducto, name="edicionProducto"),
        path('editarProducto/', editarProducto, name="editarProducto"),
        path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
]