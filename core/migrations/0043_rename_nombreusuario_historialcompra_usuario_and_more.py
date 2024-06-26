# Generated by Django 5.0.6 on 2024-06-25 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_historialcompra_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historialcompra',
            old_name='NombreUsuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='historialcompra',
            name='Comprobantes',
        ),
        migrations.AddField(
            model_name='historialcompra',
            name='detalles',
            field=models.FileField(default='Carrito', upload_to='comprobantes/'),
        ),
        migrations.AddField(
            model_name='historialcompra',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 4, 6, 45, 637295)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 25, 4, 6, 45, 637295)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 25, 4, 6, 45, 637295)),
        ),
    ]