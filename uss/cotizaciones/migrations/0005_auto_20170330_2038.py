# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 20:38
from __future__ import unicode_literals

import clientes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0004_auto_20170330_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='cliente',
            field=models.IntegerField(default=0, verbose_name=clientes.models.Cliente),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
