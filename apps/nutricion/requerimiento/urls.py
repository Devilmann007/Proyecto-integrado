from django.urls import path

from apps.nutricion.requerimiento.views import(
    requerimientoList,
    requerimientoCreate,
    requerimientoDestroy,
    requerimientoRetrieve,
    requerimientoUpdate,
)

urlpatterns =[
    path ("ruta2/",requerimientoList.as_view(), name="requerimientoList"),
    path ("ruta2/",requerimientoCreate.as_view(), name="requerimientoCreate"),
    path ("ruta2/",requerimientoDestroy.as_view(), name="requerimientoDetail"),
    path ("ruta2/",requerimientoRetrieve.as_view(), name="requerimientoRetrieve"),
    path ("ruta2/",requerimientoUpdate.as_view(), name="requerimientoUpdate"),

]