# Generated by Django 5.1.1 on 2024-10-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spcmapp', '0004_remove_reporte_code_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
