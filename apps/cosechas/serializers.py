from rest_framework import serializers
from apps.cosechas.models import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['id', 'titulo', 'contenido', 'alerta', 'fecha_generacion']