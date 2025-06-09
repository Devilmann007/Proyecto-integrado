from rest_framework import serializers
from apps.gestion_granos.procesamiento.models import EtapaProcesamiento

class ProcesamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaProcesamiento
        fields = ('id', 'lote', 'etapa', 'descripcion', 'fecha_inicio', 'fecha_fin')
