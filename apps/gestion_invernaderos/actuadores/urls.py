from django.urls import path
from apps.gestion_invernaderos.actuadores.views import ActuadorListCreateView, ActuadorRetrieveUpdateDestroyView

urlpatterns = [
    path('', ActuadorListCreateView.as_view(), name='actuadores-list-create'),
    path('<int:id_actuador>/', ActuadorRetrieveUpdateDestroyView.as_view(), name='actuadores-detail'),
]
