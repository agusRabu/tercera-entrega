from django.db import models
from categorias.models import Categoria

# esto no tiene mucho sentido porque por defecto ya hay un manejo de usuarios 
class Producto(models.Model):
    nombre_producto = models.TextField()
    stock = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return f'{self.nombre_producto} - {self.categoria} - Disponibles: {self.stock}'
