from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.calidad.views import CalidadViewSet, PruebaCalidadViewSet

router = DefaultRouter()
router.register(r'control', CalidadViewSet)
router.register(r'prueba',PruebaCalidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
