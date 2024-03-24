from django.urls import path
from .views import *
from licoreriaapp import views
from django.urls import re_path as url
from .models import *
from licoreriaapp.views import *





urlpatterns = [
    
    path('', views.home, name="Home"),
    path('articulo', views.articulo, name="Articulo"),        
    path('ventas', views.formulario, name="Ventas"),    
    path('sumar/<int:codigo_articulo>/', views.SumarCarrito, name="sumar"),    
    path('eliminar_articulo_carrito/<int:codigo_articulo>/',  views.eliminar_articulo_carrito, name="eliminar"),
    path('eliminar_articulo_carrito2/<int:codigo_articulo>/',  views.eliminar_articulo_carrito2, name="eliminar2"),
    path('restar_articulo_carrito/<int:codigo_articulo>/',  restar_articulo_carrito, name="restar"),
    path('limpiar',  limpiar, name="limpiar"),    
    path('graficos', views.graficos, name="Graficos"),
    path('registrarArticulo/', views.registrarArticulo, name="registrarArticulo"),
    path('editarArticulo/', views.editarArticulo),
    path('edicionArticulo/<codigo_articulo>', views.edicionArticulo),
    path('eliminarArticulo/<codigo_articulo>', views.eliminarArticulo),
    path('registrarVentaArticulo/', views.registrarVentaArticulo, name="registrarVentaArticulo"),
    path('contacto', views.contacto, name="Contacto"),   
    
    
    
]