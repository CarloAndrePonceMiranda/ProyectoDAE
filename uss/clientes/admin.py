from django.contrib import admin
from .models import Cliente

# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ('id', 'Razon_Social', 'Contacto', 'Telefono_1','Telefono_2','Telefono_3','Email')