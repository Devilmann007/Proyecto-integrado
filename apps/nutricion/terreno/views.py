from rest_framework import generics
from apps.nutricion.terreno.serializers import terreno
from apps.nutricion.terreno.models import terreno

class terrenoList (generics.ListAPIView):
    queryset = terreno.objects.all()
    serializer_class = terreno

class terrenoCreate (generics.CreateAPIView):
    queryset = terreno.objects.all()
    serializer_class = terreno

class terrenoRetrieve (generics.RetrieveAPIView):
    queryset = terreno.objects.all()
    serializer_class = terreno

class terrenoUpdate (generics.UpdateAPIView):
    queryset = terreno.objects.all()
    serializer_class = terreno

class terrenoDestroy (generics.DestroyAPIView):
    queryset = terreno.objects.all()
    serializer_class = terreno

    

# Create your views here.
