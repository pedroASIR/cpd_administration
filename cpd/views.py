from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from cpd.models import Sensor, Incidencia, Lectura_sensores
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your views here.

def index_view(request):
    dht11 = str(Lectura_sensores.objects.filter(sensor=1).first())
    dht22 = str(Lectura_sensores.objects.filter(sensor=2).first())
    estado_motor = str(Incidencia.objects.first())
    dht11 = dht11.split(',')
    dht22 = dht22.split(',')
    estado_motor = estado_motor.split(',')
    if estado_motor[4] == "True":
        motor = "ON"
    elif estado_motor[4] == "False":
        motor = "OFF"
    #print(dht22)
    #print(estado_motor[4])
    #print(Incidencia.objects.filter(sensor=3).first())
    dht11tem = dht11[0]
    dht11hum = dht11[1]
    dht22tem = dht22[0]
    dht22hum = dht22[1]
    context = {
        'dht11tem': dht11tem,
        'dht11hum': dht11hum,
        'dht22tem': dht22tem,
        'dht22hum': dht22hum,
        'motor': motor,
    }
    return render(request, 'index2.html', context)


def incidencias_view(request):
    incidencia = Incidencia.objects.all().order_by('id')
    context = {
        'incidencia': incidencia,
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
                incidencia.sensor=Sensor.objects.get(id = request.POST.get('sensor_id'))
                incidencia.valor_de_accion=request.POST.get('valor_de_accion')
                incidencia.descripcion=request.POST.get('descripcion')
                incidencia.estado_motor=request.POST.get('estado_motor')
                incidencia.created_at=now()
                incidencia.created_by=User.objects.get(username="pedro")
                incidencia.save()
            elif request.POST.get('tabla') == "lectura":
                lectura=Lectura_sensores()
                lectura.valorTem=request.POST.get('valorTem')
                lectura.valorHum=request.POST.get('valorHum')
                lectura.sensor=Sensor.objects.get(id = request.POST.get('sensor_id'))
                lectura.save()
            else:
                return HttpResponse("Hacen falta datos\n")
            return HttpResponse("Se han insertado correctamente los datos a la base de datos\n")
        else:
            return HttpResponse("Error en la inserción\n")
    else:
        return HttpResponse("solo post\n")