from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from clientes.models import Cliente
# Create your models here.
class Estados(models.Model):
	Estado = models.CharField(max_length=255)

def __str__(self):
        return '{}'.format(self.Estado)

class Cotizacion(models.Model):
	Fecha = models.DateField(max_length=255)
	Estado = models.ForeignKey(Estados, null=True, blank=True, on_delete=models.CASCADE)
	id_cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)


	