from rest_framework import serializers
from apps.nutricion.terreno.models import terreno

class terreno (serializers.ModelSerializer):
    class Meta:
        model = terreno
        fields = [ 'propietario', 'nombre','ubicación', 'tamaño']