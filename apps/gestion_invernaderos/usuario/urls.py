from django.urls import path  # Importamos path para definir rutas
from apps.gestion_invernaderos.usuario.views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView  # Vistas que usaremos

# Definimos las rutas disponibles para esta app
urlpatterns = [
    path('', UsuarioListCreateView.as_view(), name='usuarios-list-create'),      # /api/usuarios/
    path('<int:id_usuario>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuarios-detail'),  # /api/usuarios/1/
]

