from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from .forms import ReportForm
from licoreriaapp.precio_bcv import*

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from licoreriaapp.models import  Venta
from django.http.response import JsonResponse, HttpResponse
import json


        
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class Reporte_venta(ListView):
    model = Venta
    template_name = "reporte.html"
                                   
    def post(self, request, *args, **kwargs):
        fecha_ini = self.request.POST.get('start_date')
        fecha_fin = self.request.POST.get('end_date')                               
        # fecha_ini = '2023-12-30'
        # fecha_fin = '2024-02-02' 
                                
        if is_ajax(request=request):    
            lista = []
            for filas in Venta.objects.filter(fecha__range=(fecha_ini, fecha_fin)):
                registro = {}
                registro['codigo_venta'] = filas.codigo_venta
                registro['cliente'] = filas.cliente
                registro['ci_rif'] = filas.ci_rif
                registro['fecha'] = filas.fecha.strftime('%Y-%m-%d')
                registro['total'] = format(filas.total, '.2f')
                registro['totalbolivares'] = format(filas.totalbolivares, '.2f')
                lista.append(registro)
            # print(lista)
            return HttpResponse(json.dumps(lista), 'aplication/json')
        else:
            # print("ENTRO AQUI")
            return render(request, self.template_name)
    
    

    def get_context_data(self, **kwargs):
            x=valorDolar()
            a=x[0]
            b=x[1]
            c=x[2]
            context = super().get_context_data(**kwargs)
            context['title']= 'REPORTE DE VENTAS'
            context['entity']= 'Reportes'
            context['list_url']= reverse_lazy('reporte')
            context['form']= ReportForm()
            context['valordolar']= a
            context['valoreuro']= b
            context['fecha']= c
            return context  


