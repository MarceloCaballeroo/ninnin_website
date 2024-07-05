from django.contrib import admin
from .models import Cliente, Reserva,CarritoItem,Producto,Carrito


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(CarritoItem)
