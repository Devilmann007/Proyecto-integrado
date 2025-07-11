from django.db import models
from apps.gestion_granos.granos.models import Grano

# Create your models here.
class Lote(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    grano = models.ForeignKey(Grano, on_delete=models.CASCADE)
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.codigo