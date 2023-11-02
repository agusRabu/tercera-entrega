from django.shortcuts import render
from productos.models import Producto

def productos (request):
    return render(request, 'productos/productos.html', {})

def altaProductos (request):
    if request.method =='POST':
        nombre_producto = request.POST.get('nombre_producto')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')

        producto = Producto(nombre_producto = nombre_producto, stock = stock, categoria = categoria)
        producto.save()
    return render(request, 'productos/altaProductos.html', {})
