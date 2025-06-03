from django.db import models

class sensor (models.Model):
    tipo = models.CharField()
    descripcion =models.CharField()
    ubicacion =models.CharField()
    fecha_instal = models.DateTimeField()

    def __str__(self):
        return self.tipo

