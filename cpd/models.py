from django.db import models

# Create your models here.
from django.db.models import CASCADE

from core.models import CommonInfo


class sensor(models.Model):
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

class incidencia(CommonInfo):
    id = models.AutoField('ID', primary_key=True)
    id_sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, related_name="incidencias")
    valor_de_accion = models.IntegerField('Valor de acción')
    descripcion = models.TextField('Descripción', default='Ha saltado una alarma')
    estado_motor = models.BooleanField('Estado de los motores')
    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ['-id']

    def __str__(self):
        return self.id

class lectura_sensores(CommonInfo):
    num = models.IntegerField('Número de lectura', primary_key=True)
    id_sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, related_name="lectura_sensores")
    valor = models.SmallIntegerField('Valor de la lectura', null=False, default=0)
    class Meta:
        verbose_name = "Lectura sensor"
        verbose_name_plural = "Lectura sensores"
        ordering = ['-num']
    def __str__(self):
        return self.num

