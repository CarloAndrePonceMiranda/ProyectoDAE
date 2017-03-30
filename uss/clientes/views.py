from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class ClienteList(ListView):
    model = Cliente
class ClienteDetail(DetailView):
    model = Cliente
class ClienteCreation(CreateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list')
    fields = ['id', 'Razon_Social', 'Contacto', 'Telefono_1','Telefono_2','Telefono_3','Email']
class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list')
    fields = ['id', 'Razon_Social', 'Contacto', 'Telefono_1','Telefono_2','Telefono_3','Email']
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:list')

def principal(request):
    cliente = Cliente.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'cliente': cliente  
    }
    return HttpResponse(template.render(context, request))