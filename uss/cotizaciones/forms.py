from django import forms
from .models import Cotizacion
from django.contrib.admin import widgets

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'