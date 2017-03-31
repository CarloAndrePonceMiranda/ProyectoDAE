from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Cliente(models.Model):
	Razon_Social = models.CharField(max_length=255)
	Contacto = models.CharField(max_length=255)
	Telefono_1 = models.CharField(max_length=255)
	Telefono_2 = models.CharField(max_length=255)
	Telefono_3 = models.CharField(max_length=255)
	Email = models.CharField(max_length=255)
	
def __str__(self):
        return '{}'.format(self.Razon_Social)