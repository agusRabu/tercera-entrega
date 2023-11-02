from django.db import models

# esto no tiene mucho sentido porque por defecto ya hay un manejo de usuarios 
class Usuario(models.Model):
    nombre_usuario = models.TextField()
    nombre = models.TextField()
    apellido = models.TextField()
    ultima_vez = models.DateTimeField()
    password = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - Última conexión: {self.ultima_vez}'