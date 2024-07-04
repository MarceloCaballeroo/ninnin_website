from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Reserva, Carrito, CarritoItem, Producto
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm, ProductoForm, AddToCartForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')  

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

##################################################################################CLIENTES #########################################################################################
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
    
################################################################################# CRUD DE RESERVAS ########################################################################
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/reserva_list.html', {'reservas': reservas})


def reserva_add(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            cliente_id = request.POST.get('cliente')
            cliente = Cliente.objects.get(pk=cliente_id)
            reserva = form.save(commit=False)
            reserva.cli_reserva = cliente
            reserva.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()

    clientes = Cliente.objects.all()
    return render(request, 'reservas/reserva_add.html', {'form': form, 'clientes': clientes})

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
    

##################################################################################CARRITO#####################################################################################
@login_required
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

@login_required
def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=cantidad)
            return redirect('carrito_detail')
    else:
        form = AddToCartForm()
    return render(request, 'carrito/add_to_cart.html', {'form': form, 'producto': producto})

@login_required
def carrito_detail(request):
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    return render(request, 'carrito/carrito_detail.html', {'carrito': carrito})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('carrito_detail')
    
    # Si la solicitud es GET, podrías renderizar una plantilla de confirmación si es necesario
    
    return redirect('carrito_detail')


def confirmar_compra(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    items = carrito.items.filter(confirmado=False)

    for item in items:
        item.confirmado = True
        item.save()

    # Aquí podrías realizar otras acciones como generar una orden, enviar un correo de confirmación, etc.

    return redirect('index')  # Redirecciona a la página de confirmación o a donde sea necesario




###################################################################################################################################################################################
#####################################################################              PRODUCTOS            ###########################################################################

def producto_add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_producto')
    else:
        form = ProductoForm()
    return render(request, 'productos/producto_add.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud_producto')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_edit.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('crud_producto')
    return render(request, 'productos/producto_delete.html', {'producto': producto})


@login_required
def producto_list_usuario_comun(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'productos/productos_usuario_comun.html', context)