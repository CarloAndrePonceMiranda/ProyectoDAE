# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0006_remove_cotizacion_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nEstado', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='Estado',
        ),
    ]
