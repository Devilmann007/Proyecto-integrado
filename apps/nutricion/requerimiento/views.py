from rest_framework import generics
from apps.nutricion.requerimiento.serializers import requerimiento
from apps.nutricion.requerimiento.models import requerimiento

class requerimientoList(generics.ListAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimiento

class requerimientoCreate(generics.CreateAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimiento

class requerimientoRetrieve(generics.RetrieveAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimiento

class requerimientoUpdate(generics.UpdateAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimiento

class requerimientoDestroy(generics.DestroyAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimiento