from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('aboutUs/', include('aboutUs.urls')),
    path('admin/', admin.site.urls),
]
