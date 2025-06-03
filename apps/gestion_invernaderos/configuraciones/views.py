from rest_framework import generics
from apps.gestion_invernaderos.configuraciones.models import ConfiguracionCultivo
from apps.gestion_invernaderos.configuraciones.serializers import ConfiguracionCultivoSerializer

# Lista todas las configuraciones y permite crear nuevas
class ConfiguracionListCreateView(generics.ListCreateAPIView):
    queryset = ConfiguracionCultivo.objects.all()
    serializer_class = ConfiguracionCultivoSerializer

# Ver, editar o eliminar una configuración por ID
class ConfiguracionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfiguracionCultivo.objects.all()
    serializer_class = ConfiguracionCultivoSerializer
    lookup_field = 'id_config'
