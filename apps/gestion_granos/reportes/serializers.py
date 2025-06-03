from rest_framework import serializers
from apps.gestion_granos.reportes.models import ReporteCalidad

class ReporteCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteCalidad
        fields = '_all_'

