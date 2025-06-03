from rest_framework import generics
from apps.gestion_invernaderos.secciones.models import SeccionCultivo
from apps.gestion_invernaderos.secciones.serializers import SeccionCultivoSerializer

# Lista todas las secciones y permite crear nuevas
class SeccionListCreateView(generics.ListCreateAPIView):
    queryset = SeccionCultivo.objects.all()
    serializer_class = SeccionCultivoSerializer

# Ver, editar o eliminar una sección por su ID
class SeccionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeccionCultivo.objects.all()
    serializer_class = SeccionCultivoSerializer
    lookup_field = 'id_seccion'
