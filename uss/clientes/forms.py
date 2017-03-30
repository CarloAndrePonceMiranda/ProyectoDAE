from django import forms
from .models import Cliente
from django.contrib.admin import widgets

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'