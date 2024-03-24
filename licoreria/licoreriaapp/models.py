from django.db import models
from django.utils import timezone
from django.forms import model_to_dict

# Create your models here.

class Articulo(models.Model):      
    codigo_articulo=models.AutoField(primary_key=True)    
    articulo=models.CharField(max_length=30)
    tipo_unidad=models.CharField(max_length=30)
    cantidad=models.IntegerField(verbose_name='Cantidad', help_text = 'En stock')
    precio_sugerido_venta=models.DecimalField( decimal_places=2, default=0.0, max_digits=20, verbose_name='Precio sugerido de venta')
    class Meta:
        verbose_name ='Articulo'
        verbose_name_plural = 'Articulos'
    def __str__(self):
        return '%s Presentacion: %s stock: %s Precio: %s' %(self.articulo, self.tipo_unidad, self.cantidad, self.precio_sugerido_venta)
 
  
class Venta(models.Model):    
    codigo_venta=models.AutoField(primary_key=True)      
    cliente=models.CharField(max_length = 50, verbose_name='Cliente', null=True,)
    ci_rif=models.CharField(max_length = 20, verbose_name='Cedula o RIF', null=True)
    fecha = models.DateField()
    total=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Total')
    totalbolivares=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Total Bolivares')
    
    
    class Meta:
        verbose_name ='Venta'
        verbose_name_plural = 'Ventas'
        
    
    
    def __str__(self):
        return str( self.cliente, self.ci_rif, self.fecha, self.total )
        
    def __str__(self):
        return 'Cliente: %s Cedula-rif: %s' %(self.cliente, self.ci_rif)
    
class Venta_detalle(models.Model):
    codigo_venta=models.ForeignKey(Venta, on_delete=models.CASCADE, max_length=6)
    codigo_articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE, max_length=6)
    cantidad=models.IntegerField(verbose_name='Cantidad')
    precio_unidad=models.DecimalField( decimal_places=2, default=0.0, max_digits=20, verbose_name='Precio/unidad')
    subtotal=models.DecimalField( decimal_places=2, default=0.0, max_digits=20, verbose_name='SubTotal')
    
    def __str__(self):
        return str( self.codigo_articulo, self.cantidad, self.precio_unidad)
    def __str__(self):
        return 'Articulo: %s Cantidad: %s Pvp: %s' %(self.codigo_articulo, self.cantidad, self.precio_unidad)
    
    






    
