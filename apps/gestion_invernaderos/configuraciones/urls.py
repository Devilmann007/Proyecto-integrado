from django.urls import path
from apps.gestion_invernaderos.configuraciones.views import ConfiguracionListCreateView, ConfiguracionRetrieveUpdateDestroyView

urlpatterns = [
    path('configuraciones/', ConfiguracionListCreateView.as_view(), name='ListCreateAPIView'),
    path('<int:id_config>/', ConfiguracionRetrieveUpdateDestroyView.as_view(), name='RetrieveUpdateDestroyAPIView'),
]
