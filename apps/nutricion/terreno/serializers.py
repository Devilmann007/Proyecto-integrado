from rest_framework import serializers
from apps.nutricion.terreno.models import terreno

class terreno (serializers.ModelSerializer):
    class Meta:
        model = terreno
        fields = ['id', 'propietario', 'nombre','ubicación', 'tamaño']
        read_only_fields = ['id']