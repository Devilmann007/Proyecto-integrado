from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.riego.mantenimiento.views import (
    mantenimientoViewSet,
    historial_riegoViewSet,
)

router = DefaultRouter()
# Registra los viewsets con el router
router.register(r'historial', historial_riegoViewSet)  # ViewSet para historial de riego
router.register(r'mantenimientos', mantenimientoViewSet)  # ViewSet para mantenimientos 

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
]
