from rest_framework import serializers
from apps.gestion_granos.inventarios.models import LoteGrano

class LoteGranoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteGrano
        fields = ('id', 'tipo_grano', 'peso_kg', 'humedad_porcentaje', 'fecha_ingreso', 'observaciones')
