from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import usuarioViewSet

# Crea una instancia del enrutador por defecto
router = DefaultRouter()    

# Registra el viewset de usuario con un prefijo de URL
router.register(r'usuarios', usuarioViewSet) # ViewSet para usuarios
# Define las URL del proyecto
urlpatterns = [
    # Incluye todas las rutas generadas automáticamente por el router bajo el prefijo 'api/'
    path('', include(router.urls)),
]