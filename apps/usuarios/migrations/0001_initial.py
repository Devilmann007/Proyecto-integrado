# Generated by Django 5.2.1 on 2025-06-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('operario', 'Operario')], default='operario', max_length=20)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
