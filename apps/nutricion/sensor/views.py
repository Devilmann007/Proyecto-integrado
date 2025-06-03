from rest_framework import generics
from apps.nutricion.sensor.serializers import sensor
from apps.nutricion.sensor.models import sensor

class sensorList (generics.ListAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensor

class sensorCreate (generics.CreateAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensor

class  sensorRetrieve (generics.RetrieveAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensor

class sensorUpdate (generics.UpdateAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensor

class sensorDestroy (generics.DestroyAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensor


    
    



# Create your views here.
