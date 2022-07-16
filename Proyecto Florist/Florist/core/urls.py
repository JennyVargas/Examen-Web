from django.urls import path
from .views import eliminar_producto, limpiar_producto, principal, form_Producto, form_mod_Producto, form_del_Producto, Tienda, Tienda2, restar_producto, suscribete, usuario, Registro, contacto, registro1, agregar_producto,eliminar_producto,restar_producto,limpiar_producto, carrito

urlpatterns = [
    path('', principal, name="principal"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-Producto/<id>', form_mod_Producto, name="form_mod_Producto"),
    path('form-del-Producto/<id>', form_del_Producto, name="form_del_Producto"),
    path('Tienda', Tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="CLS"),
    path('Tienda2', Tienda2, name="Tienda2"),
    path('suscribete', suscribete, name="suscribete"),
    path('usuario', usuario, name="usuario"),
    path('Registro', Registro, name="Registro"),
    path('contacto', contacto, name="contacto"),
    path('registro1', registro1, name="registro1"),
    path('carrito', carrito, name="carrito"),
    
]
