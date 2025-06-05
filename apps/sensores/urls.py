from django.urls import path
from .views import (
    SensorListCreateView, SensorDetailView,
    LecturaListCreateView, LecturaDetailView
)

urlpatterns = [
    path('sensores/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    
    path('lecturas/', LecturaListCreateView.as_view(), name='lectura-list-create'),
    path('lecturas/<int:pk>/', LecturaDetailView.as_view(), name='lectura-detail'),
]