# Generated by Django 5.0.6 on 2024-05-25 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_tipobanco_tipocuenta_alter_compra_fechacompra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 16, 17, 30, 988687)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 16, 17, 30, 988687)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 16, 17, 30, 988687)),
        ),
    ]
