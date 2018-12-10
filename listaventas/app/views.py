from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import ProductoForm, ListaForm
from .models import ListaProducto, Producto
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

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
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = User.objects.get(username=request.user)
        post.save()
        messages.success(request, 'Tu producto ha sido añadido a la lista con éxito!')
    context = {
        'form': form
    }
    return render(request, 'registro.html', context)

def auto_lista(request):
    queryset = Producto.objects.all().filter(user=request.user)
    context = {
        "object_list": queryset
    }
    return render(request, 'lista.html', context)

def crear_lista(request):
    form = ListaForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = User.objects.get(username=request.user)
        post.save()
        messages.success(request, 'Tu lista ha sido creada con éxito!')
    context = {
        'form': form
    }
    return render(request, 'registrolista.html', context)

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

def delete(request, id):
    note = get_object_or_404(Note, pk=id).delete()
    return HttpResponseRedirect(reverse('notes.views.notes'))
