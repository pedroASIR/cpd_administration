from django.http import HttpResponse
from django.shortcuts import render
from cpd.models import Sensor, Incidencia, Lectura_sensores
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your views here.

def index_view(request):
    #dht11tem = Lectura_sensores.objects.get('valor')
    dht11 = str(Lectura_sensores.objects.filter(sensor=1).first())
    dht22 = str(Lectura_sensores.objects.filter(sensor=2).first())
    dht11=dht11.split(',')
    dht22=dht22.split(',')
    print(dht22)
    dht11tem = dht11[0]
    dht11hum = dht11[1]
    dht22tem = dht22[0]
    dht22hum = dht22[1]
    context = {
        'dht11tem': dht11tem,
        'dht11hum': dht11hum,
        'dht22tem': dht22tem,
        'dht22hum': dht22hum,
    }
    return render(request, 'index2.html', context)


def incidencias_view(request):
    incidencia = Incidencia.objects.all()
    #incidencia = incidencia.split(',')
    print(incidencia[0])

    incidencia_id = 0#incidencia[0]
    incidencia_sensor = 0#incidencia[1]
    incidencia_valor = 0#incidencia[2]
    incidencia_desc = 0#incidencia[3]
    #if incidencia[4] == "True":
    #    incidencia_motor = 'ON'
    #else:
        #incidencia_motor = 'OFF'
    incidencia_date = 0#incidencia[5]
    context = {
        'incidencia_id': incidencia_id,
        'incidencia_sensor': incidencia_sensor,
        'incidencia_valor': incidencia_valor,
        'incidencia_desc': incidencia_desc,
        'incidencia_motor': 0,#incidencia_motor,
        'incidencia_date': incidencia_date

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
                lectura.valorTem=request.POST.get('valorTem')
                lectura.valorHum=request.POST.get('valorHum')
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