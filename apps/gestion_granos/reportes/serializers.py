from rest_framework import serializers
from apps.gestion_granos.reportes.models import ReporteCalidad

class ReporteCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteCalidad
        fields = ('id', 'tipo_grano', 'fecha', 'humedad', 'impurezas', 'peso_neto', 'observaciones')

