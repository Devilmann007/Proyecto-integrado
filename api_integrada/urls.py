# proyecto/urls.py (el principal, usualmente junto a settings.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cosechas/', include('apps.cosechas.urls')),
    path('cultivo/', include('apps.nutricion.cultivo.urls')),
    path('requerimiento/', include('apps.nutricion.requerimiento.urls')),
    path('sensor/', include('apps.sensores.urls')),
    path('terreno/', include('apps.nutricion.terreno.urls')),
    path('riego/', include('apps.riego.sistema.urls')),
    path('calidad/', include('apps.gestion_granos.calidad.urls')),
    path('granos/', include('apps.gestion_granos.granos.urls')),
    path('inventarios/', include('apps.gestion_granos.inventarios.urls')),
    path('lotes/', include('apps.gestion_granos.lotes.urls')),
    path('reportes/', include('apps.gestion_granos.reportes.urls')),
    path('actuadores/', include('apps.gestion_invernaderos.actuadores.urls')),
    path('alertas/', include('apps.gestion_invernaderos.alertas.urls')),
    path('configuraciones/', include('apps.gestion_invernaderos.configuraciones.urls')),
    path('invernaderos/', include('apps.gestion_invernaderos.invernaderos.urls')),
    path('secciones/', include('apps.gestion_invernaderos.secciones.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]