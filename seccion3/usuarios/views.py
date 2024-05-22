from django.shortcuts import render, redirect
from django.template import RequestContext
from rest_framework.views import APIView
from .forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def crear_usuario(request):
    print(request)
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UsuarioForm()
    return render(request, 'crear_usuario.html', status=201)
       