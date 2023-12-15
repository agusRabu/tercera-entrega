from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.urls import reverse_lazy

from usuarios.models import Usuario, User
from usuarios.forms import FormularioAltaUsuario, FormularioEditarUsuario

def usuarios (request):
    buscador = request.GET.get('buscar')
    mensaje = None
    
    """ if buscador:
        listado_de_usuarios = User.objects.filter(
            Q(nombre_usuario__icontains=buscador.lower()) |
            Q(nombre__icontains=buscador.lower()) |
            Q(apellido__icontains=buscador.lower()) 
        )

        if not listado_de_usuarios:
            mensaje = "No se encontraron usuarios que coincidan con la búsqueda."
    else:"""
    listado_de_usuarios = User.objects.all()

    return render(request, 'usuarios/usuarios.html', {'listado_de_usuarios': listado_de_usuarios, 'mensaje': mensaje})

def altaUusarios(request):
    formulario = FormularioAltaUsuario()
    if request.method == 'POST':
        formulario = FormularioAltaUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect('login')
    return render(request, 'usuarios/altaUsuarios.html', {'formulario_de_registro': formulario})

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra  = formulario.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)
            django_login(request, user)

            usuario = Usuario.objects.get_or_create(user=request.user)

            return redirect('inicio')
    
    return render(request, 'usuarios/login.html', {'formulario_de_login': formulario})

def editarUusario(request):
    usuario = request.user.usuario

    formulario = FormularioEditarUsuario(initial={'descripcion':usuario.descripcion, 'avatar':usuario.avatar, 'link':usuario.link} , instance=request.user)
    if request.method == 'POST':
        formulario = FormularioEditarUsuario(request.POST, instance=request.user)
        if formulario.is_valid():
            
            descripcion = formulario.cleaned_data.get('descripcion')
            if descripcion:
                usuario.descripcion = descripcion
                usuario.save()
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                usuario.avatar = avatar
                usuario.save()

            link = formulario.cleaned_data.get('link')
            if link:
                usuario.link = link
                usuario.save()
            
            formulario.save()
            return redirect('inicio')
    return render(request, 'usuarios/editarUusario.html', {'formulario':formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/editarPassword.html'
    success_url = reverse_lazy('editarUusario')
