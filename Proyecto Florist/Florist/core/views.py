from imaplib import _Authenticator
from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm
from .forms import contactoForm, customUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404

# Create your views here.
from core.carrito import Carrito
from core.models import Producto


def Registro(request):
    Productos = Producto.objects.all()
    datos = {
        'Productos': Productos
    }
    
    return render(request, 'core/Registro.html', datos)


#aqui
def suscribete(request):
       
    
    return render(request, 'core/suscribete.html')

def usuario(request):
       
    
    return render(request, 'core/usuario.html')

#aqui
def Tienda2(request):
       
    
    return render(request, 'core/Tienda2.html')
#aqui
def Tienda(request):
   
    productos = Producto.objects.all()
    return render(request, 'core/Tienda.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('core/Tienda2.html')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('core/Tienda.html')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('core/Tienda.html')

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('core/Tienda.html')
#aqui 

def carrito(request):
    
    return render(request, 'core/carrito.html')

def principal(request):
    
    return render(request, 'core/principal.html')

def form_Producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_Producto.html', datos)

def form_mod_Producto(request, id):
    producto = Producto.objects.get(SKU=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_Producto.html', datos)

def form_del_Producto(request, id):
    producto = Producto.objects.get(SKU=id)
    producto.delete()
    return redirect(to="Registro")


def contacto(request):
    datos = {
        'form' : contactoForm()
    }
    if request.method == 'POST':
        formulario = contactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/contacto.html', datos)


def registro1(request):
    datos = {
        'form': customUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = customUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect (to="principal")
        datos['form'] = formulario
        
    return render(request,"registration/registro1.html", datos)
    