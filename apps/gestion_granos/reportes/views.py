
from rest_framework import viewsets
from apps.gestion_granos.reportes.models import ReporteCalidad
from apps.gestion_granos.reportes.serializers import ReporteCalidadSerializer

class ReporteCalidadViewSet(viewsets.ModelViewSet):
    queryset = ReporteCalidad.objects.all()
    serializer_class = ReporteCalidadSerializer
