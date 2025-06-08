from django.urls import path
from apps.gestion_invernaderos.alertas.views import AlertaListCreateView, AlertaRetrieveUpdateDestroyView

urlpatterns = [
    path('alertas/', AlertaListCreateView.as_view(), name='ListCreateAPIView'),
    path('<int:id_alerta>/alertas/', AlertaRetrieveUpdateDestroyView.as_view(), name='RetrieveUpdateDestroyAPIView'),
]
