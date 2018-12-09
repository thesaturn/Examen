from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class ListaProducto(models.Model):
    user = models.ForeignKey(User,default=User, on_delete=models.CASCADE)
    nombre_Lista = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nombre_Lista',)

    def __str__(self):
        return self.nombre_Lista

class Producto(models.Model):
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
    nombre_Lista = models.ForeignKey(ListaProducto, related_name='products', on_delete=models.CASCADE, default=None)
    nombre_Producto = models.CharField(max_length=200, db_index=True)
    costo_Presupuestado = models.PositiveIntegerField()
    costo_Real = models.PositiveIntegerField()
    tienda = models.CharField(max_length=200, db_index=True)
    notas = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nombre_Producto',)
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre_Producto

    def get_absolute_url(self):
        return reverse('shop2:vehiculo_list_by_marca', args=[self.slug])
