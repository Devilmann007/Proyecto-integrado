from rest_framework import serializers
from apps.nutricion.terreno.models import terreno

class terrenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = terreno
        fields = ['id', 'propietario', 'nombre','ubicacion', 'tamaño']
        read_only_fields = ['id']