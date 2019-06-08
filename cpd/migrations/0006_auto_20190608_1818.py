# Generated by Django 2.2.1 on 2019-06-08 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpd', '0005_auto_20190523_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectura_sensores',
            name='valor',
        ),
        migrations.AddField(
            model_name='lectura_sensores',
            name='valorHum',
            field=models.SmallIntegerField(default=0, null=True, verbose_name='Valor de humedad'),
        ),
        migrations.AddField(
            model_name='lectura_sensores',
            name='valorTem',
            field=models.SmallIntegerField(default=0, null=True, verbose_name='Valor de temperatura'),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidencias', to='cpd.Sensor'),
        ),
        migrations.AlterField(
            model_name='lectura_sensores',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectura_sensores', to='cpd.Sensor'),
        ),
    ]
