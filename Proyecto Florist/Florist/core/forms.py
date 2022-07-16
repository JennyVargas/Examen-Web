from django import forms
from django.forms import ModelForm 
from .models import Producto, contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['SKU', 'Nombre', 'Precio', 'Stock', 'Descripcion', 'Categoria',]
        
class contactoForm(forms.ModelForm):
     
     class Meta:
         model = contacto
         fields = ['rut', 'nombre', 'correo', 'telefono',]
                
class customUserCreationForm(UserCreationForm):
    
       class Meta:
         model = User
         fields = ['username', "first_name", "last_name", "email", "password1", "password2",]  