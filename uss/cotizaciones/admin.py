from django.contrib import admin
from .models import Cotizacion

# Register your models here.
@admin.register(Cotizacion)
class AdminCotizacion(admin.ModelAdmin):
    list_display = ('id', 'Fecha', 'Estado', 'id_cliente')
    list_filter = ('Estado',)