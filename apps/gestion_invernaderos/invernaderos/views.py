from rest_framework import generics
from apps.gestion_invernaderos.invernaderos.models import Invernadero
from apps.gestion_invernaderos.invernaderos.serializers import InvernaderoSerializer

# Vista para listar y crear invernaderos
class InvernaderoListCreateView(generics.ListCreateAPIView):
    queryset = Invernadero.objects.all()  # Trae todos los registros
    serializer_class = InvernaderoSerializer  # Serializador que convierte el modelo en JSON

# Vista para ver, actualizar o eliminar un invernadero por ID
class InvernaderoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invernadero.objects.all()
    serializer_class = InvernaderoSerializer
    lookup_field = 'id_invernadero'  # Usamos el nombre personalizado del ID


# Create your views here.
