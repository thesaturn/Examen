from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import VehiculoForm
from .models import Vehiculo
# Create your views here.

def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def registro(request):
    return render(request, 'registroauto.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'registration/login.html')

def auto_vista_test(request):
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'registro.html', context)

def auto_lista(request):
    queryset = Vehiculo.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'lista.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
