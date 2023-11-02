from django.db import models

# esto no tiene mucho sentido porque por defecto ya hay un manejo de usuarios 
class Producto(models.Model):
    nombre_producto = models.TextField()
    stock = models.TextField()
    categoria = models.IntegerField()

    def __str__(self):
        return f'{self.nombre_producto} - {self.categoria} - Disponibles: {self.stock}'
