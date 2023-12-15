from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404
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
        stock           = request.POST.get('stock')
        categoria_id    = request.POST.get('categoria')
        imagen          = request.FILES.get('imagen')
        fecha           = request.POST.get('fecha')

        categoria = get_object_or_404(Categoria, id=categoria_id)

        producto = Producto(nombre_producto = nombre_producto, stock = stock, categoria = categoria, imagen=imagen, fecha=fecha)
        producto.save()
        messages.success(request, '¡Producto Agregado!')

    return render(request, 'productos/altaProductos.html', {'categorias': categorias})

def edicionProducto(request, id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id=id)
    fecha_formateada = producto.fecha.strftime('%Y-%m-%d')
    return render(request, "productos/edicionProducto.html", {"producto": producto, 'categorias': categorias, 'fecha': fecha_formateada})

def editarProducto(request):
    if request.method == 'POST':
        id           = request.POST['idProducto']
        nombre       = request.POST['nombre_producto']
        stock        = request.POST['stock']
        categoria_id = request.POST['categoria']
        imagen       = request.FILES.get('imagen')
        fecha        =  request.POST['fecha']

        producto = Producto.objects.get(id=id)
        producto.nombre_producto = nombre
        producto.stock = stock
        

        try:
            categoria = Categoria.objects.get(id=categoria_id)
            producto.categoria = categoria
            producto.imagen = imagen
            producto.fecha = fecha
            producto.save()
            messages.success(request, '¡Producto actualizado!')
        except Categoria.DoesNotExist:
            messages.error(request, 'La categoría seleccionada no existe.')

    return redirect('/productos')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/productos')

def verMas(request, id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id=id)
    return render(request, "productos/verProducto.html", {"producto": producto, 'categorias': categorias})
