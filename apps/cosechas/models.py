from django.db import models

class ReporteAlertas(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    alerta = models.BooleanField(default=False)  # True si hay valores críticos

    def _str_(self):
        return self.titulo
    
class ConfiguracionAlertas(models.Model):
    humedad_minima = models.FloatField(default=30.0, verbose_name="Humedad Mínima Aceptable (%)")
    humedad_maxima = models.FloatField(default=70.0, verbose_name="Humedad Máxima Aceptable (%)")
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración de Alerta"
        verbose_name_plural = "Configuraciones de Alertas"

    def _str_(self):
        return f"Límites: {self.humedad_minima}%-{self.humedad_maxima}%"