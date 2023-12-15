from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import usuarios,altaUusarios, login, editarUsuario, CambiarPassword, perfil

urlpatterns = [
        path('', usuarios, name="usuarios"),
        path('altaUsuarios/', altaUusarios, name="altaUsuarios"),
        path('login/', login, name="login"),
        path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
        path('editarUsuario/', editarUsuario, name="editarUsuario"),
        path('editarPassword', CambiarPassword.as_view(), name='editarPassword'),
        path('perfil/', perfil, name="perfil"),
]