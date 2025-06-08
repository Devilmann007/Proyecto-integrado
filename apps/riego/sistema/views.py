# Importa viewsets de Django REST Framework
from rest_framework import viewsets
# Importa los modelos de la aplicación
from apps.riego.sistema.models import (
    zona_riego, configuracion_riego,
)

# Importa los serializadores de la aplicación
from apps.riego.sistema.serializers import (
    zona_riegoSerializer, 
    configuracion_riegoSerializer,
)

# ViewSet para el modelo configuracion_riego
class configuracion_riegoViewSet(viewsets.ModelViewSet):
    queryset = configuracion_riego.objects.all()  # Consulta todas las configuraciones de riego
    serializer_class = configuracion_riegoSerializer  # Serializador para el modelo configuracion_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo zona_riego
class zona_riegoViewSet(viewsets.ModelViewSet):
    queryset = zona_riego.objects.all()  # Consulta todas las zonas de riego
    serializer_class = zona_riegoSerializer  # Serializador para el modelo zona_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos
