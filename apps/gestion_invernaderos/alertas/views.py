from rest_framework import generics
from apps.gestion_invernaderos.alertas.models import Alerta
from apps.gestion_invernaderos.alertas.serializers import AlertaSerializer

class AlertaListCreateView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    lookup_field = 'id_alerta'

# Create your views here.
