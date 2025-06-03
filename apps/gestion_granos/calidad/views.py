from rest_framework import viewsets
from apps.gestion_granos.calidad.models import Calidad, PruebaCalidad
from apps.gestion_granos.calidad.serializers import calidadSerializer, PruebaCalidadSerializer

class CalidadViewSet(viewsets.ModelViewSet):
    queryset = Calidad.objects.all()
    serializer_class = calidadSerializer

class PruebaCalidadViewSet(viewsets.ModelViewSet):
    queryset = PruebaCalidad.objects.all()
    serializer_class = PruebaCalidadSerializer

