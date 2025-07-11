from rest_framework import serializers
from apps.gestion_invernaderos.invernaderos.models import Invernadero

class InvernaderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invernadero
        fields = ['id_invernadero', 'nombre', 'ubicacion', 'usuario', 'fecha_creacion']
