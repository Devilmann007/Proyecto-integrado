from django.urls import path

from apps.nutricion.cultivo.views import(
    cultivoList,
    cultivoCreate,
    cultivoDestroy,
    cultivoRetrieve,
    cultivoUpdate,
)

urlpatterns =[
    path ("ruta5/",cultivoList.as_view(), name="cultivoList"),
    path ("ruta5/",cultivoCreate.as_view(), name="cultivoCreate"),
    path ("ruta5/",cultivoDestroy.as_view(), name="cultivoDetail"),
    path ("ruta5/",cultivoRetrieve.as_view(), name="cultivoRetrieve"),
    path ("ruta5/",cultivoUpdate.as_view(), name="cultivoUpdate"),

]