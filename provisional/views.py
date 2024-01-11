from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django .urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.

# region CRUD PRODUCTO
class Listar(ListView):
    model = Producto
    template_name = "producto/listado.html"


class NuevoProducto(CreateView):
    model = Producto
    template_name = "producto/nuevo.html"
    fields = ['nombre', 'modelo', 'marca', 'unidades', 'precio', 'vip']
    success_url = reverse_lazy('listado')


class Detalles(DetailView):
    model = Producto
    template_name = "producto/detalles.html"


class Editar(UpdateView):
    model = Producto
    template_name = "producto/editar.html"
    fields = ['nombre', 'modelo', 'marca', 'unidades', 'precio', 'vip']
    success_url = reverse_lazy('listado')


class Eliminar(DeleteView):
    model = Producto
    template_name = "producto/eliminar.html"
    success_url = reverse_lazy('listado')
# endregion