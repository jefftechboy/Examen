# Generated by Django 5.0.6 on 2024-05-25 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_rename_nombrecuenta_datoscooperativos_nombrecuentacooperativo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='rutUsuario',
        ),
        migrations.AddField(
            model_name='obra',
            name='NombreUsuario',
            field=models.CharField(default='user_name', max_length=60),
        ),
        migrations.AddField(
            model_name='obra',
            name='fechaAprobada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obra',
            name='fechaRechazada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 18, 14, 45, 244689)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 18, 14, 45, 244689)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 18, 14, 45, 244689)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='razonRechazo',
            field=models.CharField(blank=True, default='----------', max_length=40, null=True),
        ),
    ]
