from rest_framework import serializers
from apps.gestion_invernaderos.secciones.models import SeccionCultivo

class SeccionCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeccionCultivo
        fields = ['id_seccion', 'nombre_seccion', 'invernadero', 'cultivo_actual']

