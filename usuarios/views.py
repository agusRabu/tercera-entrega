from datetime import datetime
from django.shortcuts import render
from usuarios.models import Usuario

def usuarios (request):
    return render(request, 'usuarios/usuarios.html')

def altaUusarios(request):
    if request.method =='POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        password = request.POST.get('password')
        ultima_vez = datetime.now()

        usuario = Usuario(nombre_usuario = nombre_usuario, nombre = nombre, apellido = apellido, password = password, ultima_vez = ultima_vez)
        usuario.save()
    return render(request, 'usuarios/altaUsuarios.html', {})