from django.urls import path

from apps.nutricion.sensor.views import(
    sensorList,
    sensorCreate,
    sensorDestroy,
    sensorRetrieve,
    sensorUpdate,
)

urlpatterns =[
    path ("ruta3/",sensorList.as_view(), name="sensorList"),
    path ("ruta3/",sensorCreate.as_view(), name="sensorCreate"),
    path ("ruta3/",sensorDestroy.as_view(), name="sensorDetail"),
    path ("ruta3/",sensorRetrieve.as_view(), name="sensorRetrieve"),
    path ("ruta3/",sensorUpdate.as_view(), name="sensorUpdate"),

]
