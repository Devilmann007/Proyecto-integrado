from rest_framework import generics
from apps.nutricion.terreno.serializers import terrenoSerializer
from apps.nutricion.terreno.models import terreno

class terrenoList (generics.ListAPIView):
    queryset = terreno.objects.all()
    serializer_class = terrenoSerializer

class terrenoCreate (generics.CreateAPIView):
    queryset = terreno.objects.all()
    serializer_class = terrenoSerializer

class terrenoRetrieve (generics.RetrieveAPIView):
    queryset = terreno.objects.all()
    serializer_class = terrenoSerializer

class terrenoUpdate (generics.UpdateAPIView):
    queryset = terreno.objects.all()
    serializer_class = terrenoSerializer

class terrenoDestroy (generics.DestroyAPIView):
    queryset = terreno.objects.all()
    serializer_class = terrenoSerializer
