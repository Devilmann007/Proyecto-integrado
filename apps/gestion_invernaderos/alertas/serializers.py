from rest_framework import serializers
from apps.gestion_invernaderos.alertas.models import Alerta

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = ['id_alerta', 'seccion', 'tipo_alerta', 'mensaje', 'fecha_hora', 'nivel_criticidad']
