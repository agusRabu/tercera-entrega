from django.shortcuts import render
from django.db.models import Q
from productos.models import Producto

def productos (request):
    buscador = request.GET.get('buscar')
    mensaje = None

    if buscador:
        listado_de_productos = Producto.objects.filter(
            Q(nombre_producto__icontains=buscador.lower()) |
            Q(categoria__icontains=buscador.lower())
        )

        if not listado_de_productos:
            mensaje = "No se encontraron productos que coincidan con la búsqueda."
    else:
        listado_de_productos = Producto.objects.all

    return render(request, 'productos/productos.html', {'listado_de_productos': listado_de_productos, 'mensaje': mensaje})

def altaProductos (request):
    if request.method =='POST':
        nombre_producto = request.POST.get('nombre_producto')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')

        producto = Producto(nombre_producto = nombre_producto, stock = stock, categoria = categoria)
        producto.save()
    return render(request, 'productos/altaProductos.html', {})
