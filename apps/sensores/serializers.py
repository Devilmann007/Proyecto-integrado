from rest_framework import serializers
from apps.gestion_invernaderos.sensores.models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id_sensor', 'tipo_sensor', 'unidad_medida', 'seccion', 'estado', 'intervalo_med']
