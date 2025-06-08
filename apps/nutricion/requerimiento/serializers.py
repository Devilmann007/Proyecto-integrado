from rest_framework import serializers
from apps.nutricion.requerimiento.models import requerimiento

class requerimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = requerimiento
        fields = ['id', 'tipo', 'tipo_de_terreno', 'fecha_de_siembra',]
        read_only_fields = ['id']