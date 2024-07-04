from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cliente(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    id_reserva = models.AutoField(db_column='idreserva', primary_key=True)
    cli_reserva = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=45)
    fecha_reserva = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Reserva de {self.nombre} para el {self.fecha_reserva} a las {self.hora}'
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    confirmado = models.BooleanField(default=False)  # Campo para indicar si el item ha sido confirmado

    def subtotal(self):
        return self.cantidad * self.producto.precio


