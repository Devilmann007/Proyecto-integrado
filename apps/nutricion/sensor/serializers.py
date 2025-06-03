from rest_framework import serializers
from apps.nutricion.sensor.models import sensor

class sensor(serializers.ModelSerializer):

    model = sensor

    fields = ['id','descripcion','ubicacion','fecha_instal']