# alumnos/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'mysite/Pages/index.html')

def comidas(request):
    return render(request, 'mysite/Pages/comidas.html')

def promociones(request):
    return render(request, 'mysite/Pages/Promociones.html')

def reservacion(request):
    return render(request, 'mysite/Pages/Reservacion.html')

def sucursal(request):
    return render(request, 'mysite/Pages/Sucursal.html')


@login_required
def menu(request):
    request.session["usuario"] = "Jcampos"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'administrador/menu.html',context)