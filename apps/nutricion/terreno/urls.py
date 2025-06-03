from django.urls import path

from apps.nutricion.terreno.views import(
    terrenoList,
    terrenoCreate,
    terrenoDestroy,
    terrenoRetrieve,
    terrenoUpdate,
)

urlpatterns =[
    path ("ruta4/",terrenoList.as_view(), name="terrenoList"),
    path ("ruta4/",terrenoCreate.as_view(), name="terrenoCreate"),
    path ("ruta4/",terrenoDestroy.as_view(), name="terrenoDetail"),
    path ("ruta4/",terrenoRetrieve.as_view(), name="terrenoRetrieve"),
    path ("ruta4/",terrenoUpdate.as_view(), name="terrenoUpdate"),

]