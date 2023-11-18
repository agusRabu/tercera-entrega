from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from productos.models import Producto
from categorias.models import Categoria

def productos (request):
    buscador = request.GET.get('buscar')
    mensaje = None

    if buscador:
        listado_de_productos = Producto.objects.filter(
            Q(nombre_producto__icontains=buscador.lower()) |
            Q(categoria__nombre_categoria__icontains=buscador.lower())
        )

        if not listado_de_productos:
            mensaje = "No se encontraron productos que coincidan con la búsqueda."
    else:
        listado_de_productos = Producto.objects.all

    return render(request, 'productos/productos.html', {'listado_de_productos': listado_de_productos, 'mensaje': mensaje})

def altaProductos (request):
    categorias = Categoria.objects.all()
    if request.method =='POST':
        nombre_producto = request.POST.get('nombre_producto')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')

        producto = Producto(nombre_producto = nombre_producto, stock = stock, categoria = categoria)
        producto.save()
        messages.success(request, '¡Producto Agregado!')

    return render(request, 'productos/altaProductos.html', {'categorias': categorias})

def edicionProducto(request, nombre):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(nombre_producto=nombre)
    return render(request, "productos/edicionProducto.html", {"producto": producto, 'categorias': categorias})

def editarProducto(request):
    id = request.POST['idProducto']
    nombre = request.POST['nombre_producto']
    stock = request.POST['stock']
    categoria = request.POST['categoria']

    producto = Producto.objects.get(id=id)
    producto.nombre_producto = nombre
    producto.stock = stock
    producto.categoria = categoria
    producto.save()
    messages.success(request, '¡Producto actualizado!')

def eliminarProducto(request, nombre):
    producto = Producto.objects.get(nombre_producto=nombre)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')
