# Generated by Django 5.1.1 on 2024-10-24 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('no_empleado', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('admin', 'Admin'), ('engineer', 'Engineer'), ('technician', 'Technician')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.CharField(max_length=100)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=150)),
                ('codigo_cliente', models.CharField(max_length=100)),
                ('resina_1', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('resina_2', models.CharField(blank=True, max_length=100, null=True)),
                ('Maquina', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ruta', models.CharField(max_length=100)),
                ('Descripcion_1', models.CharField(max_length=100)),
                ('Categoria', models.CharField(max_length=100)),
                ('Operación', models.IntegerField()),
                ('Subcontratacion', models.CharField(max_length=100)),
                ('Centro_trabajo_ppal', models.CharField(max_length=100)),
                ('Destino_ope', models.CharField(max_length=100)),
                ('Cod_maquina', models.CharField(max_length=100)),
                ('Tipo_tpo_operacional', models.CharField(max_length=100)),
                ('Tiempo_ajuste', models.FloatField()),
                ('Tpo_operacional', models.FloatField()),
                ('Cadencia', models.FloatField()),
                ('Cadence_theo', models.CharField(max_length=100)),
                ('Utillaje', models.CharField(max_length=100)),
                ('Eficiencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.CharField(max_length=150)),
                ('content', models.JSONField()),
                ('formato', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spcmapp.producto')),
                ('producto_maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spcmapp.producto_maquina')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        
    ]
