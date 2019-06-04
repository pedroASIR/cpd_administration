from django.http import HttpResponse
from django.shortcuts import render
from cpd.models import Sensor, Incidencia, Lectura_sensores
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your views here.

def index_view(request):
    context = {
        'sample_var': "ejemplo"
    }
    return render(request, 'index2.html', context)


def incidencias_view(request):
    context = {

    }
    return render(request, 'incidencias.html', context)


@csrf_exempt
def insert_database(request):
    if request.method == 'POST':
        if request.POST.get('tabla'):
            if request.POST.get('tabla') == "sensor":
                sensor=Sensor()
                sensor.id=request.POST.get('id')
                sensor.nombre=request.POST.get('nombre')
                sensor.tipo=request.POST.get('tipo')
                sensor.estado=request.POST.get('estado')
                sensor.valor_max_tem=request.POST.get('valor_max_tem')
                sensor.save()
            elif request.POST.get('tabla') == "incidencia":
                incidencia= Incidencia()
                #incidencia.id=request.POST.get('id')
                incidencia.sensor=Sensor.objects.get(id = request.POST.get('sensor_id'))
                incidencia.valor_de_accion=request.POST.get('valor_de_accion')
                incidencia.descripcion=request.POST.get('descripcion')
                incidencia.estado_motor=request.POST.get('estado_motor')
                incidencia.created_at=now()
                incidencia.created_by=User.objects.get(username="pedro")
                incidencia.save()
            elif request.POST.get('tabla') == "lectura":
                lectura=Lectura_sensores()
                lectura.valor=request.POST.get('valor')
                lectura.sensor=Sensor.objects.get(id = request.POST.get('sensor_id'))
                #lectura.created_at=now()
                #lectura.created_by=User.objects.get(username="pedro")
                lectura.save()
            else:
                return HttpResponse("Hacen falta datos\n")
            return HttpResponse("Se han insertado correctamente los datos a la base de datos\n")
        else:
            return HttpResponse("Error en la inserción\n")
    else:
        return HttpResponse("solo post\n")