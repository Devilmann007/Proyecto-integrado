from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.inventarios.views import LoteGranoViewSet

router = DefaultRouter()
router.register(r'lotes', LoteGranoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
