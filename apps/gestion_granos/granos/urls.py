from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.gestion_granos.granos.views import GranoViewSet

router = DefaultRouter()
router.register(r'granos', GranoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
