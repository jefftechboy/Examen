# Generated by Django 5.0.6 on 2024-05-25 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_obra_rutusuario_obra_nombreusuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 19, 12, 30, 259789)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 19, 12, 30, 259789)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 19, 12, 30, 259789)),
        ),
    ]
