from rest_framework import viewsets
from apps.cosechas.models import ReporteAlertas, ConfiguracionAlertas
from apps.cosechas.serializers import ReporteSerializer, ConfiguracionAlertasSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = ReporteAlertas.objects.all()
    serializer_class = ReporteSerializer
    

class AlertasViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionAlertas.objects.all()
    serializer_class = ConfiguracionAlertasSerializer
    