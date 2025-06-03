from rest_framework import serializers
from apps.nutricion.requerimiento.models import requerimiento

class requerimiento(serializers.ModelSerializer):
    class Meta:
        model = requerimiento
        fields = ['tipo', 'tipo de terreno', 'fecha de siembra']