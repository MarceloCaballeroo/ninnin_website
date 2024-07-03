from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Reserva
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
        form = ReservaForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # Limpiar form
            form = ReservaForm(user=request.user)
            context = {'mensaje': "Ok, datos grabados..", "form": form}
        else:
            context = {'form': form}
    else:
        form = ReservaForm(user=request.user)
        context = {'form': form}
    return render(request, "clientes/reserva.html", context)


def clientes_del (request,pk):
    context={}
    try:
        cliente = Cliente.objects.get(id=pk)

        cliente.delete()
        mensaje = "Datos de cliente eliminados"
        clientes = Cliente.objects.all()
        context = {'clientes' : clientes, 'mensaje' : mensaje}
        return render(request,'clientes/clientes_list.html',context)
    except:
        mensaje="Error, id no existe..."
        clientes = Cliente.objects.all()
        context = {'clientes' : clientes, 'mensaje': mensaje }
        return render(request, 'clientes/clientes_list.html', context)
    

def clientes_findEdit(request,pk):
    if pk != "":
        cliente = Cliente.objects.get(id=pk)
        user = User.objects.all()

        print(type(cliente.nombre))

        context={'cliente':cliente, 'user':user }
        if cliente:
            return render(request, 'clientes/clientes_edit.html',context)
        else:
                context={'mensaje':"Error, id no existe"}
                return render(request, 'clientes/cliente_list.html', context)
        

def clientesUpdate(request):
    if request.method == "POST":
        id = request.POST.get("ID")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        email = request.POST.get("correo")
        password = request.POST.get("password")
        user_id = request.POST.get("IDuser")

        try:
            cliente = Cliente.objects.get(id=id)
            cliente.nombre = nombre
            cliente.apellido = apellido
            cliente.fecha_nacimiento = fecha_nacimiento
            cliente.email = email
            cliente.password = password
            cliente.user_id = user_id
            cliente.save()

            context = {'mensaje': "Datos actualizados", 'cliente': cliente}
            return render(request, 'clientes/clientes_edit.html', context)
        except Cliente.DoesNotExist:
            context = {'mensaje': "Error, cliente no existe"}
            return render(request, 'clientes/clientes_list.html', context)
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'clientes/clientes_list.html', context)

def clientesAdd(request):
    if request.method != "POST":
        users = User.objects.all()  # Obtener todos los usuarios
        context = {'users': users}
        return render(request, 'clientes/clientes_add.html', context)
    else:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        email = request.POST.get("correo")
        password = request.POST.get("password")
        user_id = request.POST.get("user")

        if not user_id:
            context = {'mensaje': "Seleccione un usuario", 'users': User.objects.all()}
            return render(request, 'clientes/clientes_add.html', context)

        cliente = Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password=password,
            user_id=user_id
        )

        context = {'mensaje': "Cliente añadido", 'users': User.objects.all()}
        return render(request, 'clientes/clientes_add.html', context)
    




def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/reserva_list.html', {'reservas': reservas})

def reserva_add(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_reserva = request.POST.get('fecha_reserva')
        hora = request.POST.get('hora')
        cliente_id = request.POST.get('cliente')  # Obtener el ID del cliente desde el formulario

        cliente = Cliente.objects.get(pk=cliente_id)  # Obtener el objeto Cliente usando su ID
        reserva = Reserva(nombre=nombre, email=email, telefono=telefono, fecha_reserva=fecha_reserva, hora=hora, cli_reserva=cliente)
        reserva.save()

        return redirect('reserva_list')

    # Obtener todos los clientes para mostrar en el formulario
    clientes = Cliente.objects.all()
    return render(request, 'reservas/reserva_add.html', {'clientes': clientes})

def reserva_update(request, pk):
    reserva = get_object_or_404(Reserva, id_reserva=pk)

    if request.method == 'POST':
        reserva.nombre = request.POST.get('nombre')
        reserva.email = request.POST.get('email')
        reserva.telefono = request.POST.get('telefono')
        reserva.fecha_reserva = request.POST.get('fecha_reserva')
        reserva.hora = request.POST.get('hora')
        reserva.save()

        return redirect('reserva_list')

    return render(request, 'reservas/reserva_update.html', {'reserva': reserva})


def reserva_del(request, pk):
    reserva = get_object_or_404(Reserva, id_reserva=pk)
    reserva.delete()
    return redirect('reserva_list')


@login_required
def custom_redirect(request):
    if request.user.is_staff:
        return redirect('crud')  # Redirigir a la página CRUD
    else:
        return redirect('index')