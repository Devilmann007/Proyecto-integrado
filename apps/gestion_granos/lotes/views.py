from rest_framework import viewsets
from apps.gestion_granos.lotes.models import Lote
from apps.gestion_granos.lotes.serializers import LoteSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer