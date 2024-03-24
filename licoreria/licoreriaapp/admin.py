from django.contrib import admin

from .models import  Articulo, Venta, Venta_detalle

class ArticuloAdmin(admin.ModelAdmin):
    ordering =('articulo',)
    search_fields=('articulo','tipo_unidad','codigo_articulo','cantidad')
    list_filter=('tipo_unidad',)
   
   
class VentaAdmin(admin.ModelAdmin):
    ordering=['cliente']
    search_fields=('cliente','ci_rif',)
    list_filter=('cliente', 'fecha',)
    
    
class Venta_detalleAdmin(admin.ModelAdmin):
    ordering=['codigo_venta']
    #search_fields=('cliente','ci_rif',)
    #list_filter=('cliente', 'fecha',)
    autocomplete_fields=['codigo_articulo']

    

# Register your models here.


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Venta_detalle, Venta_detalleAdmin)

