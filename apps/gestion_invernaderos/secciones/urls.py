from django.urls import path
from apps.gestion_invernaderos.secciones.views import SeccionListCreateView, SeccionRetrieveUpdateDestroyView

urlpatterns = [
    path('secciones/', SeccionListCreateView.as_view(), name='ListCreateAPIView'),  
    path('<int:id_seccion>/secciones', SeccionRetrieveUpdateDestroyView.as_view(), name='RetrieveUpdateDestroyAPIView'),
]