from django.db import models

# Create your models here.

class cultivo(models.Model):

    tipo = models.CharField ()
    fecha_siembra =models.DateField ()
    fecha_cosecha = models.DateField ()
    nombre_terreno = models.CharField ()

    def __str__(self):
        return self.cultivo
 
