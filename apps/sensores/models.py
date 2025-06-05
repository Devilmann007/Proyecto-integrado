from django.db import models

class Sensor(models.Model):
    TIPO_CHOICES = [
        ('humedad', 'Humedad del Aire'),
        ('temperatura', 'Temperatura'),
        ('lluvia', 'Lluvia'),
        ('humedad_suelo', 'Humedad del Suelo'),
        # Puedes agregar más tipos aquí
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        help_text='Tipo de sensor (humedad, temperatura, lluvia, etc.)'
    )
    descripcion = models.CharField(max_length=100, blank=True)
    ubicacion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)     # Activo/Inactivo
    fecha_instalacion = models.DateTimeField()
    ultima_lectura = models.FloatField(default=0.0)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.get_tipo_display()} ({self.ubicacion})"

class LecturaSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    unidad = models.CharField(
        max_length=10,
        choices=[('porcentaje', 'Porcentaje'), ('grados', 'Grados')],
        default='porcentaje'
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.sensor.get_tipo_display()} - {self.valor} {self.unidad} @ {self.fecha_hora}"