from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class ProductoList(ListView):
    model = Producto
    instances = Producto.objects.all().order_by('id')
class ProductoDetail(DetailView):
    model = Producto
class ProductoCreation(CreateView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    fields = ['id', 'Medida_Diametro', 'Armazon', 'Precio','Tela']
    instances = Producto.objects.all().order_by('id')
class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    fields = ['id', 'Medida_Diametro', 'Armazon', 'Precio','Tela']
    instances = Producto.objects.all().order_by('id')
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    instances = Producto.objects.all().order_by('id')

def principal(request):
    producto = Producto.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'producto': producto  
    }
    return HttpResponse(template.render(context, request))