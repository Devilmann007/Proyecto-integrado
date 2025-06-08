from django.db import models

class requerimiento(models.Model):
    tipo = models.CharField (max_length=100)
    tipo_de_terreno = models.CharField (max_length=100)
    fecha_de_siembra = models.DateField ()

    def __str__(self):
        return f"{self.tipo} - {self.tipo_de_terreno}"
        # Retorna el tipo de requerimiento