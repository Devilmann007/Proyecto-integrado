from django.urls import path

from apps.nutricion.requerimiento.views import(
    requerimientoList,
    requerimientoCreate,
    requerimientoDestroy,
    requerimientoRetrieve,
    requerimientoUpdate,
)

urlpatterns = [
    # GET List Listar objetos (todos)
    path("requerimientos/", requerimientoList.as_view(), name="ListAPIView"),
    # POST create 	Crear un nuevo objeto    
    path("create/", requerimientoCreate.as_view(), name="CreateAPIView"), 
    # GET retrieve Obtener un objeto por su ID 
    path("<int:pk>/requerimientos/", requerimientoRetrieve.as_view(), name="RetrieveAPIView"),
    # PUT/PATCH Actualizar un objeto existente  
    path("<int:pk>/update/", requerimientoUpdate.as_view(), name="UpdateAPIView"),
    # DELETE Eliminar un objeto por su ID  
    path("<int:pk>/delete/", requerimientoDestroy.as_view(), name="DestroyAPIView"), 
]
# Tambien podemos usar ListCreateAPIView (GET, POST) Lista y crea objetos
# RetrieveUpdateDestroyAPIView (GET, PUT, PATCH, DELETE) Todo sobre un objeto específico