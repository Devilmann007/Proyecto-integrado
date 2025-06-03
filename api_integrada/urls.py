# proyecto/urls.py (el principal, usualmente junto a settings.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cosechas/', include('apps.cosechas.urls')),
    path('administrador/', include('apps.nutricion.administrador.urls')),
    path('cultivo/', include('apps.nutricion.cultivo.urls')),
    path('requerimiento/', include('apps.nutricion.requerimiento.urls')),
    path('sensor/', include('apps.nutricion.sensor.urls')),
    path('terreno/', include('apps.nutricion.terreno.urls')),
    path('riego/', include('apps.riego.sistema.urls')),
]