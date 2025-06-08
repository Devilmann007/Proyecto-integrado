from rest_framework import serializers
from apps.gestion_granos.lotes.models import Lote

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ('id', 'codigo', 'grano', 'cantidad_kg', 'fecha_ingreso')
