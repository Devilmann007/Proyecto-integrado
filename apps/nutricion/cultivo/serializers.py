from rest_framework import serializers
from apps.nutricion.cultivo.models import cultivo

class cultivoserializers(serializers.ModelSerializer):
    class Meta: 
        model = cultivo
        fields = ['id', 'tipo' , 'fecha_siembra','fecha_cosecha','nombre_terreno']
        read_only_fields = ['id']


       