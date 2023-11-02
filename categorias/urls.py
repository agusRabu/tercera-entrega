from django.urls import path
from categorias.views import categorias, altaCategorias

urlpatterns = [
        path('', categorias, name="categorias"),
        path('altaCategorias/', altaCategorias, name="altaCategorias"),
]