from django.urls import path, re_path
from .views import *
from licoreriaapp import views
# from .views import ArticuloAutocomplete
# from dal import autocomplete
from django.urls import re_path as url
from django.db import models
from .models import *
# from licoreriaapp.views import agregarVenta
from django.shortcuts import render, HttpResponse





urlpatterns = [
    
   
    path('', registro_usuario.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    path('base3', base3, name="base3"),
    
    
]