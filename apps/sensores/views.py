from rest_framework import generics
from apps.sensores.models import Sensor
from apps.sensores.serializers import SensorSerializer

# Listar todos los sensores y crear nuevos
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Obtener, editar o eliminar un sensor por ID
class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
