from django.db import models

# Create your models here.
class terreno (models.Model):

    nombre = models.CharField (max_length=100)
    propietario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tamaño = models.FloatField( help_text="Tamaño del terreno en hectáreas (por ejemplo: 2.5).")

    def __str__(self):
        return self.terreno 