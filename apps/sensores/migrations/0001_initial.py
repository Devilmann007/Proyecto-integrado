# Generated by Django 5.2.1 on 2025-06-07 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('humedad', 'Humedad del Aire'), ('temperatura', 'Temperatura'), ('lluvia', 'Lluvia'), ('humedad_suelo', 'Humedad del Suelo')], help_text='Tipo de sensor (humedad, temperatura, lluvia, etc.)', max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_instalacion', models.DateTimeField()),
                ('ultima_lectura', models.FloatField(default=0.0)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LecturaSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unidad', models.CharField(choices=[('porcentaje', 'Porcentaje'), ('grados', 'Grados')], default='porcentaje', max_length=10)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturas', to='sensores.sensor')),
            ],
        ),
    ]
