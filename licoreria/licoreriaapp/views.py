
from django.shortcuts import HttpResponse as HttpResponse, render, HttpResponse, redirect, get_object_or_404
from licoreriaapp.models import Articulo, Venta, Venta_detalle
from django.contrib import messages
from django.db.models import Q
from licoreriaapp.precio_bcv import*
from licoreriaapp.carrito import Carrito
from django.contrib.auth.decorators import login_required   
    


def registrarVentaArticulo(request):
    # print('entro')
    if request.POST:
        fecha_venta = request.POST['fecha']
        cedula = request.POST['ci']
        nombre = request.POST['cliente']
        dolares = float(request.POST['total'])
        bolivares = float(request.POST['totalbolivares'])
        venta_nueva = Venta(fecha=fecha_venta, cliente=nombre, ci_rif=cedula,  total=dolares, totalbolivares=bolivares)
        venta_nueva.save()
        items=request.POST['detalle'].split("@")
        for item in items:
            elementos = item.split(";")
            articulo_id = int(elementos[0])
            cantidad_ = int(elementos[1])
            pvp = float(elementos[2])
            subtotal = float(elementos[3])
            nuevo_detalle=Venta_detalle( codigo_venta_id=venta_nueva.codigo_venta, codigo_articulo_id=articulo_id, cantidad=cantidad_, precio_unidad=pvp, subtotal=subtotal)   
            nuevo_detalle.save()            
            edicion=Articulo.objects.get(codigo_articulo=articulo_id)           
            edicion.cantidad=edicion.cantidad-cantidad_
            edicion.save()              
        # messages.success(request, '!Venta registrada!')        
        return HttpResponse("OK")
    return HttpResponse("metodo no permitido")



def formulario(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    context={'valordolar':a, 'valoreuro':b, 'fecha': c}
    # print('cliente')
    return render(request,"licoreriaapp/ventas.html", context)




def home(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    context={'valordolar':a, 'valoreuro':b, 'fecha': c}
    return render(request, "licoreriaapp/home.html", context)

def contacto(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    context={'valordolar':a, 'valoreuro':b, 'fecha': c}
    return render(request, "licoreriaapp/contacto.html", context)

def articulo(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    articulo=Articulo.objects.all()
    template_name='licoreriaapp/articulo.html'
    context={'articulo':articulo, 'valordolar':a, 'valoreuro':b, 'fecha': c}
    # print('cliente paso')
    return render(request, template_name,context)


def SumarCarrito(request, codigo_articulo):
    articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    # print(articulo,'articulo', type(articulo))
    carrito=Carrito(request)
    carrito.sumar(request, codigo_articulo, articulo)
    return redirect("Ventas")


def eliminar_articulo_carrito(request, codigo_articulo):
    carrito=Carrito(request)
    carrito.eliminar(codigo_articulo)
    return redirect("Ventas")

def eliminar_articulo_carrito2(request, codigo_articulo):
    carrito=Carrito(request)
    carrito.eliminar2(codigo_articulo)
    return redirect("Ventas")

def restar_articulo_carrito(request, codigo_articulo):
    articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    carrito=Carrito(request)
    carrito.restar(codigo_articulo, articulo)
    return redirect("Ventas")

def limpiar(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("Ventas")



def graficos(request):
    return render(request, "graficos.html")

def edicionArticulo(request,codigo_articulo):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    template_name='licoreriaapp/edicionarticulo.html'
    context={'articulo':articulo, 'valordolar':a, 'valoreuro':b, 'fecha': c}
    # print('cliente paso')
    return render(request, template_name,context)


    
    
    

def registrarArticulo(request):
    articulo=request.POST['articulo']
    tipo_unidad=request.POST['tipo_unidad']
    cantidad=request.POST['cantidad']
    precio_sugerido_venta=request.POST['precio_sugerido_venta']
    articulo_grabar=Articulo.objects.create(articulo=articulo, tipo_unidad=tipo_unidad, cantidad=cantidad, precio_sugerido_venta=precio_sugerido_venta)
    messages.success(request, '!Articulo registrado!')
    return redirect('/articulo')


def editarArticulo(request):
    codigo_articulo=request.POST['codigo_articulo']
    articulo=request.POST['articulo_editar']
    tipo_unidad=request.POST['tipo_unidad_editar']
    cantidad=request.POST['cantidad']
    precio_venta_sugerido=request.POST['precio_sugerido_venta_editar']
    edicion=Articulo.objects.get(codigo_articulo=codigo_articulo)
    edicion.articulo=articulo
    edicion.tipo_unidad=tipo_unidad
    edicion.cantidad=cantidad
    edicion.precio_sugerido_venta=precio_venta_sugerido
    edicion.save()
    messages.success(request, '!Articulo editado!')
    return redirect('/articulo')



def eliminarArticulo(request,codigo_articulo):
    codigo_articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    codigo_articulo.delete()
    messages.success(request, '!Articulo eliminado!')
    return redirect('/articulo')











