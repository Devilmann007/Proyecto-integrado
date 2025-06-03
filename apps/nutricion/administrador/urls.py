from django.urls import path

from apps.nutricion.administrador.views import(
    administradorList,
    administradorCreate,
    administradorDestroy,
    administradorRetrive,
    administradorUpdate,
)

urlpatterns =[
    path ("ruta1/",administradorList.as_view(), name="administradorList"),
    path ("ruta2/",administradorCreate.as_view(), name="administradorCreate"),
    path ("ruta3/",administradorDestroy.as_view(), name="administradorDetail"),
    path ("ruta4/",administradorRetrive.as_view(), name="administradorRetrieve"),
    path ("ruta5/",administradorUpdate.as_view(), name="adminitradorUpdate"),

]

