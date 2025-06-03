from rest_framework import generics
from apps.gestion_invernaderos.lecturas.models import LecturaSensor
from apps.gestion_invernaderos.lecturas.serializers import LecturaSensorSerializer

# Vista para listar y crear lecturas
class LecturaListCreateView(generics.ListCreateAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer

# Vista para ver, editar o eliminar una lectura por ID
class LecturaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer
    lookup_field = 'id_lectura'


# Create your views here.
