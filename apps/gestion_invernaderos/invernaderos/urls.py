from django.urls import path
from apps.gestion_invernaderos.invernaderos.views import InvernaderoListCreateView, InvernaderoRetrieveUpdateDestroyView

urlpatterns = [
    path('invernaderos/', InvernaderoListCreateView.as_view(), name='invernaderos-list-create'),
    path('<int:id_invernadero>/invernaderos/', InvernaderoRetrieveUpdateDestroyView.as_view(), name='invernaderos-detail'),
]
