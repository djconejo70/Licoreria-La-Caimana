from django.shortcuts import render, HttpResponse, redirect
from licoreriaapp.models import Inventario_guardia, Articulo
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from .forms import ArticuloForm
from django.http import HttpRequest
# Create your views here.

def home(request):
    return render(request, "licoreriaapp/home.html")

def articulo(request):
    articulo=Articulo.objects.all()
    template_name='licoreriaapp/articulo.html'
    context={'articulo':articulo}    
    return render(request, template_name,context)


def guardia(request):
    guardia=Inventario_guardia.objects.all()
    return render(request, "licoreriaapp/guardia.html", {'guardia':guardia})

def graficos(request):

    return render(request, "licoreriaapp/graficos.html")

def edicionArticulo(request,codigo_articulo):
    articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    return render(request, "licoreriaapp/edicionArticulo.html", {"articulo":articulo})




class ArticuloFormView(HttpRequest):
    def index(request):        
        articulo=ArticuloForm()        
        return render(request, "licoreriaapp/articulo.html", {"form":articulo})
    def procesar_formulario(request):
        articulo=ArticuloForm(request.POST)
        if articulo.is_valid():
            articulo.save()
            articulo=ArticuloForm()
        return render(request, "licoreriaapp/articulo.html", {"form":articulo, "mensaje": 'OK'})
        
           

def editarArticulo(request):
    codigo_articulo=request.POST['codigo_articulo']
    articulo=request.POST['articulo']
    tipo_unidad=request.POST['tipo_unidad']
    cantidad=request.POST['cantidad']
    edicion=Articulo.objects.get(codigo_articulo=codigo_articulo)
    edicion.articulo=articulo
    edicion.tipo_unidad=tipo_unidad
    edicion.cantidad=cantidad
    edicion.save()
    messages.success(request, '!Articulo editado!', extra_tags='tag1 tag2')     
    return redirect('/articulo')
    


def eliminarArticulo(request,codigo_articulo):
    codigo_articulo=Articulo.objects.get(codigo_articulo=codigo_articulo)
    codigo_articulo.delete()
    messages.success(request, '!Articulo eliminado!')
    return redirect('/articulo')








