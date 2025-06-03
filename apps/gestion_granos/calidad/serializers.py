from rest_framework import serializers
#from .models import PruebaCalidad
from apps.gestion_granos.calidad.models import Calidad, PruebaCalidad

class calidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calidad
        fields = '__all__'

class PruebaCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calidad, #PruebaCalidad
        fields = '__all__'
