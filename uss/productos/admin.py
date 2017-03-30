from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('id', 'Medida_Diametro', 'Armazon', 'Tela', 'Precio')
    list_filter = ('Medida_Diametro','Armazon', 'Tela',)