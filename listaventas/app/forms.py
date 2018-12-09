from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Producto, ListaProducto

class ListaForm(forms.ModelForm):
    class Meta:
        model = ListaProducto
        exclude =  ['user','slug']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
        'nombre_Producto',
        'costo_Presupuestado',
        'costo_Real',
        'tienda',
        'notas',
        'nombre_Lista',
        ]

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Contraseña")
