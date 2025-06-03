from rest_framework import generics
from apps.gestion_invernaderos.actuadores.models import ActuadorRiego
from apps.gestion_invernaderos.actuadores.serializers import ActuadorRiegoSerializer

# Listar y crear actuadores
class ActuadorListCreateView(generics.ListCreateAPIView):
    queryset = ActuadorRiego.objects.all()
    serializer_class = ActuadorRiegoSerializer

# Ver, editar o eliminar un actuador por ID
class ActuadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActuadorRiego.objects.all()
    serializer_class = ActuadorRiegoSerializer
    lookup_field = 'id_actuador'
