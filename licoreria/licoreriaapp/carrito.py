import simplejson as json
from django.contrib import messages

class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session 
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}        
        self.carrito=carrito
            
    def agregar(self, articulo):
        if ((str(articulo.codigo_articulo) not in self.carrito.keys())) and (articulo.cantidad>0):
            self.carrito[articulo.codigo_articulo]={
                "codigo_articulo":articulo.codigo_articulo,
                "articulo":articulo.articulo,
                # "acumulado":articulo.cantidad,
                "unidades":1,
                "cantidad":articulo.cantidad,                
                # "precio_sugerido_venta":articulo.precio_sugerido_venta,
                "precio_sugerido_venta" : float(articulo.precio_sugerido_venta), # or float(d)
                "subtotal" : float(articulo.precio_sugerido_venta),                            
            }
        else:
            for key,value in self.carrito.items():
                if key == str(articulo.codigo_articulo) and (articulo.cantidad>value["unidades"]):
                    value["unidades"] = value["unidades"]+1
                    value["subtotal"] = value["subtotal"]+ float(articulo.precio_sugerido_venta)
                    break
                # else:
                    # messages.warning(self, '!No existe STOCK adecuado!')                 
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True
        
    def eliminar(self, codigo_articulo):
        id=str(codigo_articulo)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito
    
    def eliminar2(self, codigo_articulo):
        for key, value in self.carrito.items():
            if key==str(codigo_articulo):
                self.eliminar(codigo_articulo)
                break
        self.guardar_carrito()
            
    def restar(self, codigo_articulo, articulo):
        for key, value in self.carrito.items():
            if key==str(codigo_articulo):
                value["unidades"]=value["unidades"]-1
                value["subtotal"]=float(value["subtotal"]) - float(articulo.precio_sugerido_venta)
                if value["unidades"]<1:                    
                    self.eliminar(codigo_articulo)                    
                break
        self.guardar_carrito()
            
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True
        
    def sumar(self, codigo_articulo, articulo, request):
        # print('paso x suma') 
        # print(codigo_articulo, 'codigo_articulo')
        
        # print(value.unidades, 'value unidades')
        
        subtotal=0.0     
        for key, value in self.carrito.items():
            # print(value["cantidad"], 'value cantidad')
            # print(value["unidades"], 'value unidades')
            # print(key, 'key')
            # print(articulo, type(articulo), 'articulo y tipo')
            if (key == str(articulo)) and (value["unidades"]<value["cantidad"]):
                # print('entro if carrito')
                value["unidades"] = value["unidades"]+1
                # print('entro', value["unidades"], value["precio_sugerido_venta"] )
                value["subtotal"] = value["subtotal"]+ float(value["precio_sugerido_venta"])
                break
            elif (key == str(articulo)) and (value["unidades"]>=value["cantidad"]):
                # print('paso aqui warning')
                messages.success(self.request, '!No existe STOCK adecuado!')
                            
        self.guardar_carrito()
            
        
        