from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Productos

# Create your views here.
class listaProductos(ListView):
    model = Productos
    paginate_by = 10