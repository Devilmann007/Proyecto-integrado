from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.cosechas.views import ReporteViewSet, AlertasViewSet

router = DefaultRouter()

router.register(r'reporteAlertas', ReporteViewSet)
router.register(r'configuracionAlertas', AlertasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



