

from core.models import Producto


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    def agregar(self,producto):
        id =str(producto.id)
        if id not in self.carrito.Keys():
            self.carrito[id]={
                "SKU": Producto.SKU,
                "nombre": Producto.Nombre,
                "acumulado": Producto.Precio,
                "stock": 1,
            }
        else:
            self.carrito[id]["Stock"]  += 1
            self.carrito[id]["acumulado"] += Producto.Precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
            
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.Keys():
            self.carrito[id]["Stock"] -= 1
            self.carrito[id]["acumulado"] -= Producto.Precio
            if self.carrito[id]["Stock"] <= 0: 
                self.eliminar(Producto)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True