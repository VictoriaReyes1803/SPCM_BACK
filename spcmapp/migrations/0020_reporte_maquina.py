# Generated by Django 5.1.1 on 2024-12-18 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spcmapp', '0019_maquina_planta'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='maquina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spcmapp.maquina'),
        ),
    ]