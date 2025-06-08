from django.urls import path
from apps.sensores.views import (
    SensorListCreateView, SensorRetrieveUpdateDestroyView
)

urlpatterns = [
    path('sensores/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorListCreateView.as_view(), name='sensor-detail'),
    
    path('lecturas/', SensorRetrieveUpdateDestroyView.as_view(), name='lectura-list-create'),
    path('lecturas/<int:pk>/', SensorRetrieveUpdateDestroyView.as_view(), name='lectura-detail'),
]