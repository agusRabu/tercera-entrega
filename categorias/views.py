from datetime import datetime
from django.shortcuts import render
from categorias.models import Categoria

def categorias (request):
    listado_de_categorias = Categoria.objects.all
    
    return render(request, 'categorias/categorias.html',{'listado_de_categorias': listado_de_categorias})

def altaCategorias(request):
    if request.method =='POST':
        nombre_categoria = request.POST.get('nombre_categoria')
    
        categoria = Categoria(nombre_categoria = nombre_categoria.lower())
        categoria.save()
    return render(request, 'categorias/altaCategorias.html', {})