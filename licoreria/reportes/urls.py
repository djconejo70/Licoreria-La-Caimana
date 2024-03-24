from django.urls import path
from reportes.views import *



urlpatterns = [
    
    
    path('reporte', Reporte_venta.as_view(), name="reporte"),
    
    
    
    
]