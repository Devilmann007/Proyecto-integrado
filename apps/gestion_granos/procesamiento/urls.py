from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.procesamiento.views import ProcesamientoViewSet

router = DefaultRouter()
router.register(r'Procesamiento', ProcesamientoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]