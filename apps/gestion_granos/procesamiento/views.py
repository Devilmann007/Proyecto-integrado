
from rest_framework import viewsets
from apps.gestion_granos.procesamiento.models import EtapaProcesamiento
from apps.gestion_granos.procesamiento.serializers import ProcesamientoSerializer

class ProcesamientoViewSet(viewsets.ModelViewSet):
    queryset = EtapaProcesamiento.objects.all()
    serializer_class = ProcesamientoSerializer

