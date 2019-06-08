from django.db import models

# Create your models here.
from django.db.models import CASCADE

from core.models import CommonInfo


class Sensor(models.Model):
    TIPO_CHOICES = (
        ("TEM", "Temperatura"),
        ("HUM", "Humedad"),
        ("GAS", "Gas"),
        ("LLA", "Llama"),
    )
    id = models.AutoField('ID', primary_key=True)
    nombre = models.CharField('Nombre', max_length=10, null=False)
    tipo = models.CharField('Tipo', max_length=3, choices=TIPO_CHOICES, null=False)
    estado = models.BooleanField('Estado', null=False, default=True)
    valor_max_tem = models.SmallIntegerField('Valor Máximo de Temperatura', null=True)

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"
        ordering = ['-nombre']
    
    def __str__(self):
        return self.nombre

class Incidencia(CommonInfo):
    id = models.AutoField('ID', primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="incidencias")
    valor_de_accion = models.IntegerField('Valor de acción')
    descripcion = models.TextField('Descripción', default='Ha saltado una alarma')
    estado_motor = models.BooleanField('Estado de los motores')
    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ['-id']

    def __str__(self):
        cadena = str(self.id)+','+str(self.sensor)+','+str(self.valor_de_accion)+','+self.descripcion+','+str(self.estado_motor)+','+str(self.created_at)
        return cadena

class Lectura_sensores(CommonInfo):
    num = models.AutoField('Número de lectura', primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="lectura_sensores")
    valorTem = models.SmallIntegerField('Valor de temperatura', null=True, default=0)
    valorHum = models.SmallIntegerField('Valor de humedad', null=True, default=0)
    class Meta:
        verbose_name = "Lectura sensor"
        verbose_name_plural = "Lectura sensores"
        ordering = ['-num']
    def __str__(self):
        valores = str(self.valorTem) + ', ' + str(self.valorHum)
        return valores
