# Importa la función 'path' para definir rutas y 'include' para incluir rutas de otros módulos
from django.urls import path, include

# Importa el enrutador por defecto de Django REST Framework
from rest_framework.routers import DefaultRouter

# Importa los viewsets de la aplicación
from apps.riego.sistema.views import (
    zona_riegoViewSet,
    configuracion_riegoViewSet,
)

# Crea una instancia del enrutador por defecto
router = DefaultRouter()

# Registra cada viewset con un prefijo de URL
router.register(r'zonas', zona_riegoViewSet)  # ViewSet para zonas de riego
router.register(r'configuraciones', configuracion_riegoViewSet)  # ViewSet para configuraciones de riego

# Define las URL del proyecto
urlpatterns = [
    # Incluye todas las rutas generadas automáticamente por el router bajo el prefijo 'api/'
    path('', include(router.urls)),
]
