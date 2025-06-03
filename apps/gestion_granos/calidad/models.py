from django.db import models
# Create your models here.
class Calidad(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    producto = models.CharField(max_length=100)  # Ej: Maíz, Trigo, Soya
    origen = models.CharField(max_length=100)    # Ej: Finca, proveedor, región
    fecha_recepcion = models.DateField()
    peso_total_kg = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.codigo} - {self.producto} ({self.fecha_recepcion})'


class PruebaCalidad(models.Model):
    lote = models.ForeignKey(Calidad, on_delete=models.CASCADE)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    impurezas = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=100)
    fecha_prueba = models.DateField()

    def __str__(self):
        return f'Prueba de calidad - {self.lote.codigo}'
