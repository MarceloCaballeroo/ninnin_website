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
    cli_reserva = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=45)
    fecha_reserva = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Reserva de {self.nombre} para el {self.fecha_reserva} a las {self.hora}'
