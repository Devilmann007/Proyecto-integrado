from rest_framework import serializers
from apps.gestion_invernaderos.actuadores.models import ActuadorRiego

class ActuadorRiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuadorRiego
        fields = ['id_actuador', 'tipo_actuador', 'seccion', 'estado', 'fecha_activacion']
