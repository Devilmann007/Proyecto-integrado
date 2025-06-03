
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.reportes.views import ReporteCalidadViewSet

router = DefaultRouter()
router.register(r'reportes', ReporteCalidadViewSet, basename='reporte')

urlpatterns = [
    path('', include(router.urls)),
]
