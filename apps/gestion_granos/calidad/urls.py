from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.calidad.views import CalidadViewSet

router = DefaultRouter()
router.register(r'Calidad', CalidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
