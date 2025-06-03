from rest_framework import serializers
from apps.gestion_granos.granos.models import Grano

class GranoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grano
        fields = '__all__'