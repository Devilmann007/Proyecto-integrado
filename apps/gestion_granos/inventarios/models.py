from django.db import models

class LoteGrano(models.Model):
    TIPO_GRANO_CHOICES = [
        ('maiz', 'Maíz'),
        ('trigo', 'Trigo'),
        ('soja', 'Soja'),
    ]

    tipo_grano = models.CharField(max_length=20, choices=TIPO_GRANO_CHOICES)
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    humedad_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_ingreso = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lote {self.id} - {self.tipo_grano}"
