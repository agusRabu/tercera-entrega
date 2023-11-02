from django.db import models

# esto no tiene mucho sentido porque por defecto ya hay un manejo de usuarios 
class Categoria(models.Model):
    nombre_categoria = models.TextField()

    def __str__(self):
        return f'{self.nombre_categoria}'