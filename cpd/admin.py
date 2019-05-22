from django.contrib import admin

# Register your models here.
from cpd.models import sensor, incidencia, lectura_sensores

admin.site.register(sensor)
admin.site.register(incidencia)
admin.site.register(lectura_sensores)