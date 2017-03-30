from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	Medida_Diametro = models.CharField(max_length=255)
	Armazon = models.CharField(max_length=255)
	Precio = models.DecimalField(max_digits=10,decimal_places=2)
	Tela = models.CharField(max_length=255)