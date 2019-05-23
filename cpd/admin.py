from django.contrib import admin

# Register your models here.
from cpd.models import Sensor, Incidencia, Lectura_sensores

admin.site.register(Sensor)
admin.site.register(Incidencia)
admin.site.register(Lectura_sensores)