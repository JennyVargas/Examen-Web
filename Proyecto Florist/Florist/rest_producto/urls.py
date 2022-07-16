from django.urls import path
from rest_producto.views import lista_Producto, detalle_producto
from rest_producto.viewslogin import login


urlpatterns =[
    path('lista_Producto', lista_Producto, name="lista_Producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name="login"),
    ]