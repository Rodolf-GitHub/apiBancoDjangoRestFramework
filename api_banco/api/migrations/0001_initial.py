# Generated by Django 4.2.2 on 2023-07-05 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=30, unique=True)),
                ('contrasena', models.CharField(max_length=16)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('estado', models.CharField(default='pendiente', max_length=30)),
                ('descripcion', models.CharField(max_length=180)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('salario', models.IntegerField()),
                ('direccion', models.CharField(max_length=60)),
                ('personas_sustento', models.IntegerField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('salario_anual', models.IntegerField()),
                ('cant_trabajadores', models.IntegerField()),
                ('nombre_director', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('codigo', models.CharField(max_length=60)),
                ('nombre_empresa', models.CharField(max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
