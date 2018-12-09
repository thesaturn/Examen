from django.db import models
from django.urls import reverse


class Marca(models.Model):
    marca = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('marca',)
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.marca

    def get_absolute_url(self):
        return reverse('shop2:vehiculo_list_by_marca', args=[self.slug])

class Color(models.Model):
    color = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('color',)
        verbose_name = 'color'
        verbose_name_plural = 'colores'

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('shop2:vehiculo_list_by_color', args=[self.slug])


class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, related_name='products', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, related_name='products', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200, db_index=True)
    año = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, db_index=True)
    descripción = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=0)
    número_Puertas = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    fecha_de_Publicación = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_de_Publicación',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse('shop2:vehiculo_detail', args=[self.id, self.slug])
