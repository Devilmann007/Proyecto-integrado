# proyecto/urls.py (el principal, usualmente junto a settings.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cosechas/', include('apps.cosechas.urls')),
    path('cultivo/', include('apps.nutricion.cultivo.urls')),
    path('requerimiento/', include('apps.nutricion.requerimiento.urls')),
    path('sensores/', include('apps.sensores.urls')),
    path('terreno/', include('apps.nutricion.terreno.urls')),
    path('riego/', include('apps.riego.sistema.urls')),
    path('mantenimiento/', include('apps.riego.mantenimiento.urls')),
    path('calidad/', include('apps.gestion_granos.calidad.urls')),
    path('grano/', include('apps.gestion_granos.granos.urls')),
    path('inventarios/', include('apps.gestion_granos.inventarios.urls')),
    path('procesamiento/', include ('apps.gestion_granos.procesamiento.urls')),
    path('lote/', include('apps.gestion_granos.lotes.urls')),
    path('reportes/', include('apps.gestion_granos.reportes.urls')),
    path('alerta/', include('apps.gestion_invernaderos.alertas.urls')),
    path('configuracion/', include('apps.gestion_invernaderos.configuraciones.urls')),
    path('invernadero/', include('apps.gestion_invernaderos.invernaderos.urls')),
    path('seccion/', include('apps.gestion_invernaderos.secciones.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]