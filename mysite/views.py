# alumnos/views.py

from django.shortcuts import render

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


