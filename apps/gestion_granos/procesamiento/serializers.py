from rest_framework import serializers
from apps.gestion_granos.procesamiento.models import EtapaProcesamiento

class ProcesamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaProcesamiento
        fields = '__all__'
