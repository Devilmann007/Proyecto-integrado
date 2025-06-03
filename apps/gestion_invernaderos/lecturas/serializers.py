from rest_framework import serializers
from apps.gestion_invernaderos.lecturas.models import LecturaSensor

class LecturaSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaSensor
        fields = ['id_lectura', 'sensor', 'valor', 'fecha_hora']
