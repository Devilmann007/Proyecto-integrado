from rest_framework import serializers
from apps.nutricion.administrador.models import usuario

class usuarioseralizado(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = [
            'id','nombre','apellido','correo','telefono','rol'
        ]
