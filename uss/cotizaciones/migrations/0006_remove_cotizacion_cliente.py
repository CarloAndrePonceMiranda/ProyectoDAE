# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0005_auto_20170330_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='cliente',
        ),
    ]
