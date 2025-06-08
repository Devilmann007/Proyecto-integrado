from django.urls import path

from apps.nutricion.cultivo.views import(
    cultivoCreateAPIView,
    cultivoListAPIView,
    cultivoDestroyAPIView,
    cultivoRetrieveAPIView,
    cultivoUpdateAPIView,
)

urlpatterns = [
    # GET List Listar objetos (todos)
    path("cultivos/", cultivoListAPIView.as_view(), name="ListAPIView"),
    # POST create 	Crear un nuevo objeto    
    path("create/", cultivoCreateAPIView.as_view(), name="CreateAPIView"), 
    # GET retrieve Obtener un objeto por su ID 
    path("<int:pk>/cultivos/", cultivoRetrieveAPIView.as_view(), name="RetrieveAPIView"),
    # PUT/PATCH Actualizar un objeto existente  
    path("<int:pk>/update/", cultivoUpdateAPIView.as_view(), name="UpdateAPIView"),
    # DELETE Eliminar un objeto por su ID  
    path("<int:pk>/delete/", cultivoDestroyAPIView.as_view(), name="DestroyAPIView"), 
]
# Tambien podemos usar ListCreateAPIView (GET, POST) Lista y crea objetos
# RetrieveUpdateDestroyAPIView (GET, PUT, PATCH, DELETE) Todo sobre un objeto específico
