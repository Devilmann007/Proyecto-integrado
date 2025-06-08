from django.urls import path

from apps.nutricion.terreno.views import(
    terrenoList,
    terrenoCreate,
    terrenoDestroy,
    terrenoRetrieve,
    terrenoUpdate,
)

urlpatterns = [
    # GET List Listar objetos (todos)
    path("terrenos/", terrenoList.as_view(), name="ListAPIView"),
    # POST create 	Crear un nuevo objeto    
    path("create/", terrenoCreate.as_view(), name="CreateAPIView"), 
    # GET retrieve Obtener un objeto por su ID 
    path("<int:pk>/terrenos/", terrenoRetrieve.as_view(), name="RetrieveAPIView"),
    # PUT/PATCH Actualizar un objeto existente  
    path("<int:pk>/update/", terrenoUpdate.as_view(), name="UpdateAPIView"),
    # DELETE Eliminar un objeto por su ID  
    path("<int:pk>/delete/", terrenoDestroy.as_view(), name="DestroyAPIView"), 
]
# Tambien podemos usar ListCreateAPIView (GET, POST) Lista y crea objetos
# RetrieveUpdateDestroyAPIView (GET, PUT, PATCH, DELETE) Todo sobre un objeto específico