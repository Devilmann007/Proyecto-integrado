from django.urls import path
from apps.gestion_invernaderos.sensores.views import SensorListCreateView, SensorRetrieveUpdateDestroyView

urlpatterns = [
    path('', SensorListCreateView.as_view(), name='sensores-list-create'),
    path('<int:id_sensor>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensores-detail'),
]
