from rest_framework import generics  # Importamos clases genéricas ya construidas
from apps.gestion_invernaderos.usuario.models import Usuario          # Nuestro modelo de usuarios
from apps.gestion_invernaderos.usuario.serializers import UsuarioSerializer  # Nuestro serializador

# Vista para listar usuarios y crear nuevos (GET y POST)
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()         # Qué datos queremos listar
    serializer_class = UsuarioSerializer     # Con qué serializador convertiremos esos datos

# Vista para ver, editar o eliminar un solo usuario (GET, PUT, DELETE)
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()         # Qué datos permitimos consultar
    serializer_class = UsuarioSerializer     # Serializador que transforma esos datos
    lookup_field = 'id_usuario'              # Le decimos que el ID del modelo se llama así (no "id")
