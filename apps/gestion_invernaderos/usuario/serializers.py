from rest_framework import serializers  # Módulo para crear serializadores
from apps.gestion_invernaderos.usuario.models import Usuario             # Importamos el modelo que queremos serializar

# Creamos una clase basada en ModelSerializer (que nos ahorra mucho trabajo)
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # Indicamos qué modelo vamos a serializar
        fields = ['id_usuario', 'nombre', 'correo', 'contraseña', 'rol', 'fecha_registro']  
        # Definimos qué campos queremos mostrar o aceptar
