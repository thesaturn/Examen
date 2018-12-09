from django.contrib import admin
from .models import Producto, ListaProducto

class ListaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Lista']
    prepopulated_fields = {'slug':('nombre_Lista',)}
admin.site.register(ListaProducto, ListaProductoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Producto','costo_Presupuestado', 'costo_Real', 'tienda', 'notas','slug']
    prepopulated_fields = {'slug':('nombre_Producto',)}
admin.site.register(Producto, ProductoAdmin)
