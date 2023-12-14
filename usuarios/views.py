from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.db.models import Q
from usuarios.models import Usuario
from usuarios.forms import FormularioAltaUsuario

def usuarios (request):
    buscador = request.GET.get('buscar')
    mensaje = None
    
    if buscador:
        listado_de_usuarios = Usuario.objects.filter(
            Q(nombre_usuario__icontains=buscador.lower()) |
            Q(nombre__icontains=buscador.lower()) |
            Q(apellido__icontains=buscador.lower()) 
        )

        if not listado_de_usuarios:
            mensaje = "No se encontraron usuarios que coincidan con la búsqueda."
    else:
        listado_de_usuarios = Usuario.objects.all()

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

            return redirect('inicio')
    
    return render(request, 'usuarios/login.html', {'formulario_de_login': formulario})