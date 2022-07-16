from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

# modelo para el Producto
class Producto(models.Model):
    SKU = models.CharField(max_length=6, primary_key=True, verbose_name='SKU')
    Nombre  = models.CharField(max_length=20, verbose_name='Nombre Producto')
    Precio = models.CharField(max_length=20, null=True, blank=True, verbose_name='Precio')
    Stock =  models.CharField(max_length=20, null=True, blank=True, verbose_name='Stock')
    Descripcion =  models.CharField(max_length=50, null=True, blank=True, verbose_name='Descripción')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.SKU


class contacto(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut')
    nombre = models.CharField( max_length=50, verbose_name='Nombre')
    correo =  models.EmailField()
    telefono = models.CharField(max_length=13, verbose_name='Telefono')
    
    def __str__(self):
        return self.rut
    
    
    
    
    
    
    
# username: Florist
#Password: jclecb123