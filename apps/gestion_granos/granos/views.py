from rest_framework import viewsets
from apps.gestion_granos.granos.models import Grano
from apps.gestion_granos.granos.serializers import GranoSerializer

class GranoViewSet(viewsets.ModelViewSet):
    queryset = Grano.objects.all()
    serializer_class = GranoSerializer

