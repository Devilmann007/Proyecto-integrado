from rest_framework import serializers
from apps.cosechas.models import ReporteAlertas, ConfiguracionAlertas

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteAlertas
        fields = ('id', 'titulo', 'contenido','fecha_generacion', 'alerta')

class ConfiguracionAlertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionAlertas
        fields = ('id', 'humedad_minima', 'humedad_maxima', 'ultima_actualizacion')
