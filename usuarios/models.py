from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    descripcion = models.CharField(max_length=300, default='')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, default='default.jpg')
    link = models.URLField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - Última conexión: {self.ultima_vez}'