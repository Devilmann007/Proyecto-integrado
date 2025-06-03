from rest_framework import viewsets
from apps.gestion_granos.inventarios.models import LoteGrano
from apps.gestion_granos.inventarios.serializers import LoteGranoSerializer

class LoteGranoViewSet(viewsets.ModelViewSet):
    queryset = LoteGrano.objects.all().order_by('-fecha_ingreso')
    serializer_class = LoteGranoSerializer
