from django.db import models

# Create your models here.
class terreno (models.Model):

    nombre = models.CharField ()
    propietario = models.CharField()
    ubicacion = models.CharField()
    tamaño = models.FloatField()

    def __str__(self):
        return self.terreno 