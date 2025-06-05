from rest_framework import serializers
from .models import Sensor
from .models import LecturaSensor

class SensorSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Sensor
        fields = [
            'id',
            'tipo',
            'tipo_display',
            'descripcion',
            'ubicacion',
            'estado',
            'fecha_instalacion',
            'ultima_lectura',
            'ultima_actualizacion',
        ]
        read_only_fields = ['id']


class LecturaSensorSerializer(serializers.ModelSerializer):
    sensor_tipo = serializers.CharField(source='sensor.get_tipo_display', read_only=True)
    sensor_ubicacion = serializers.CharField(source='sensor.ubicacion', read_only=True)

    class Meta:
        model = LecturaSensor
        fields = [
            'id',
            'sensor',
            'sensor_tipo',
            'sensor_ubicacion',
            'valor',
            'unidad',
            'fecha_hora',
        ]
        read_only_fields = ['id']