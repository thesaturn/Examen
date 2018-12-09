from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
        'marca',
        'modelo',
        'año',
        'color',
        'número_Puertas',
        'descripción',
        'precio',
        ]
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Contraseña")
