# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='IDcliente',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
