from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes/login')
    else:
        form = UserCreationForm()
    return render(request, 'Clientes/register.html', {'form': form})