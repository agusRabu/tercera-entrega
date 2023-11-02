from django.urls import path
from usuarios.views import usuarios,altaUusarios

urlpatterns = [
        path('', usuarios, name="usuarios"),
        path('altaUsuarios/', altaUusarios, name="altaUsuarios"),
]