from django.db import models
#from ckeditor.fields import RichTextField
from categorias.models import Categoria

class Producto(models.Model):
    nombre_producto = models.TextField()
    stock = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True, default='default.jpg')
    fecha = models.DateField(null=True, blank=True, default=None)
    #formateado = RichTextField(blank=True,default=None)

    def __str__(self):
        return f'{self.nombre_producto} - {self.categoria} - Disponibles: {self.stock}'
