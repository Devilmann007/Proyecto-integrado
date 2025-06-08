from rest_framework import generics
from apps.nutricion.cultivo.serializers import cultivoserializers
from apps.nutricion.cultivo.models import cultivo

class cultivoListAPIView(generics.ListAPIView): # GET Listar objetos (todos)
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers
    

class cultivoCreateAPIView(generics.CreateAPIView): # POST create 	Crear un nuevo objeto
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoRetrieveAPIView(generics.RetrieveAPIView): # GET retrieve Obtener un objeto por su ID 
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoUpdateAPIView(generics.UpdateAPIView):   # PUT/PATCH Actualizar un objeto existente 
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoDestroyAPIView(generics.DestroyAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers
    


