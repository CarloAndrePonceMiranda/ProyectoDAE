# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0002_auto_20170330_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='id_cliente',
            field=models.IntegerField(),
        ),
    ]
