
from django.db import models

class ReporteCalidad(models.Model):
    TIPO_GRANO_CHOICES = [
        ('maiz', 'Maíz'),
        ('arroz', 'Arroz'),
        ('trigo', 'Trigo'),
        ('soya', 'Soya'),
    ]

    tipo_grano = models.CharField(max_length=20, choices=TIPO_GRANO_CHOICES)
    fecha = models.DateField()
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    impurezas = models.DecimalField(max_digits=5, decimal_places=2)
    peso_neto = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo_grano} - {self.fecha}"

