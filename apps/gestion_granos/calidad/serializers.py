from rest_framework import serializers
#from .models import PruebaCalidad
from apps.gestion_granos.calidad.models import Calidad, PruebaCalidad

class calidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calidad
        fields = ('id', 'codigo', 'producto', 'fecha_recepcion', 'peso_total_kg', 'observaciones')

class PruebaCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaCalidad
        fields = ('id', 'lote', 'humedad', 'impurezas', 'color', 'fecha_prueba')
