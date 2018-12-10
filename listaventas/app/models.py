from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class ListaProducto(models.Model):
    user = models.ForeignKey(User,default=User, on_delete=models.CASCADE)
    nombre_Lista = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nombre_Lista',)

    def __str__(self):
        return self.nombre_Lista

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.nombre_Lista)
        super(ListaProducto, self).save(*args, **kwargs)

class Producto(models.Model):
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
    nombre_Lista = models.ForeignKey(ListaProducto, related_name='products', on_delete=models.CASCADE, default='asd')
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

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.nombre_Producto)
        super(Producto, self).save(*args, **kwargs)
