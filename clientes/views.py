from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirige a la página de inicio después de iniciar sesión
        else:
            # si la autenticación falla, puedes mostrar un mensaje de error
            return render(request, 'Clientes/login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'Clientes/login.html')


def registro(request):
    if request.method != "POST":
        context={"clase": "registro"}
        return render(request, 'clientes/registro.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'clientes/registro.html', context)
    
def galeria(request):
    context={"clase": "galeria"}
    return render(request, 'clientes/galeria.html', context)

def crud_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes' : clientes}
    return render(request, 'clientes/clientes_list.html',context)

#preparacion vista final
@login_required
def menu(request):
    request.session["usuario"] = "Jcampos"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'clientes/clientes_list.html',context)
      
def reserva_Form(request):
    print("estoy en el controlador reserva...")
    context = {}

    if request.method == "POST":
        print("controlador es un post...")
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            # Limpiar form
            form =ReservaForm()
            context = {'mensaje': "Ok, datos grabados..", "form": form}
        else:
            context = {'form': form}
    else:
        form = ReservaForm()
        context = {'form': form}
    return render(request, "clientes/reserva.html", context)

