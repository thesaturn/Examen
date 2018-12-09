from django.contrib import admin
from .models import Marca, Color, Vehiculo

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['marca','slug']
    prepopulated_fields = {'slug':('marca',)}
admin.site.register(Marca, MarcaAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ['color','slug']
    prepopulated_fields = {'slug':('color',)}
admin.site.register(Color, ColorAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['modelo','marca','color','slug','precio','número_Puertas','disponible','fecha_de_Publicación']
    list_filter = ['marca','color','disponible','fecha_de_Publicación']
    list_editable = ['precio','disponible']
    prepopulated_fields = {'slug':('modelo',)}
admin.site.register(Vehiculo, VehiculoAdmin)
