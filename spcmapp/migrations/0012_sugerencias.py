# Generated by Django 5.1.1 on 2024-12-04 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spcmapp', '0011_reporte_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sugerencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugerencia', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]