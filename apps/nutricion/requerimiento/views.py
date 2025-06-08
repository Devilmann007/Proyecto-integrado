from rest_framework import generics
from apps.nutricion.requerimiento.serializers import requerimientoSerializer
from apps.nutricion.requerimiento.models import requerimiento

class requerimientoList(generics.ListAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimientoSerializer

class requerimientoCreate(generics.CreateAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimientoSerializer

class requerimientoRetrieve(generics.RetrieveAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimientoSerializer

class requerimientoUpdate(generics.UpdateAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimientoSerializer

class requerimientoDestroy(generics.DestroyAPIView):
    queryset = requerimiento.objects.all()
    serializer_class = requerimientoSerializer