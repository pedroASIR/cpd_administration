# Generated by Django 2.2.1 on 2019-05-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpd', '0002_auto_20190522_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidencia',
            old_name='id_sensor',
            new_name='sensor',
        ),
        migrations.RenameField(
            model_name='lectura_sensores',
            old_name='id_sensor',
            new_name='sensor',
        ),
    ]
