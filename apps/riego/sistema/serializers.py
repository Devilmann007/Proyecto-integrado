# Importa el módulo serializers de Django REST Framework
from rest_framework import serializers
# Importa los modelos definidos en la aplicación 'sistema'
from apps.riego.sistema.models import (
    zona_riego,
    configuracion_riego,
)

# Serializador para el modelo configuracion_riego
class configuracion_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuracion_riego  # Modelo a serializar
        fields = ('id', 'frecuencia', 'hora_inicio', 'duracion', 'tipo_riego', 'caudal', 'presion')
        read_only_fields = ['id']
        

# Serializador para el modelo zona_riego
class zona_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = zona_riego  # Modelo a serializar
        fields = ('id', 'nombre_zona', 'tipo_planta', 'necesidades_hidricas', 'exposicion_solar')
        read_only_fields = ['id']  # id solo lectura

# Fin del archivo sistema/serializers.py
