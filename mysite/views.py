# alumnos/views.py

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'mysite/Pages/index.html')

def comidas(request):
    return render(request, 'mysite/Pages/comidas.html')

def promociones(request):
    return render(request, 'mysite/Pages/Promociones.html')



def sucursal(request):
    return render(request, 'mysite/Pages/Sucursal.html')


