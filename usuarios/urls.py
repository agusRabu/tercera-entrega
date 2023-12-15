from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import usuarios,altaUusarios, login, editarUusario, CambiarPassword

urlpatterns = [
        path('', usuarios, name="usuarios"),
        path('altaUsuarios/', altaUusarios, name="altaUsuarios"),
        path('login/', login, name="login"),
        path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
        path('editarUusario/', editarUusario, name="editarUusario"),
        path('editarPassword', CambiarPassword.as_view(), name='editarPassword')
]