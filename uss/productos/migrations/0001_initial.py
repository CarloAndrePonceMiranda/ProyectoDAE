# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medida_Diametro', models.CharField(max_length=255)),
                ('Armazon', models.CharField(max_length=255)),
                ('Tela', models.CharField(max_length=255)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
