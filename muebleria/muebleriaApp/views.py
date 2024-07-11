from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Producto , Carrito
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect


def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('productos')
    else:
        form = UserCreationForm()
    return render(request, 'registrarse.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('template')  
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('template')

def template(request):
    return render(request, 'template.html')

def nosotros(request):
    return render(request, 'nosotros.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def agregar_a_carrito(request, producto_id, cantidad):
    producto = get_object_or_404(Producto, id=producto_id)
    item_carrito, created = Carrito.objects.get_or_create(producto=producto)
    
    if created:
        item_carrito.cantidad = int(cantidad)
    else:
        item_carrito.cantidad += int(cantidad)
    
    item_carrito.save()
    return redirect('ver_carrito')

def editar_carrito(request, carrito_id):
    item_carrito = get_object_or_404(Carrito, id=carrito_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        item_carrito.cantidad = cantidad
        item_carrito.save()
        return redirect('ver_carrito')
    return render(request, 'editar_carrito.html', {'item': item_carrito})

def eliminar_del_carrito(request, carrito_id):
    item_carrito = get_object_or_404(Carrito, id=carrito_id)
    item_carrito.delete()
    return redirect('ver_carrito')

def ver_carrito(request):
    items = Carrito.objects.all()
    return render(request, 'carrito.html', {'carrito': items})


@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        tel = request.POST.get('tel')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        suscripcion = request.POST.get('suscripcion')

        # Redirigir a una página de éxito o mostrar un mensaje de éxito
        return HttpResponseRedirect('/gracias/')
    return render(request, 'contact_form.html')