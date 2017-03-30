from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cotizacion(models.Model):
	Fecha = models.DateField(max_length=255)
	Estado = models.CharField(max_length=255)
	IDcliente = models.IntegerField()
	