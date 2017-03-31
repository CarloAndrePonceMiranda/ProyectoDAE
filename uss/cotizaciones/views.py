from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Cotizacion
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class CotizacionList(ListView):
    model = Cotizacion
class CotizacionDetail(DetailView):
    model = Cotizacion
class CotizacionCreation(CreateView):
    model = Cotizacion
    success_url = reverse_lazy('cotizaciones:list')
    fields = ['id', 'Fecha', 'Estado', 'id_cliente']
    Cotizacion.objects.order_by('id')
class CotizacionUpdate(UpdateView):
    model = Cotizacion
    success_url = reverse_lazy('cotizaciones:list')
    fields = ['id', 'Fecha', 'Estado', 'id_cliente']
class CotizacionDelete(DeleteView):
    model = Cotizacion
    success_url = reverse_lazy('cotizaciones:list')

def principal(request):
    cliente = Cotizacion.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'cliente': cliente  
    }
    return HttpResponse(template.render(context, request))