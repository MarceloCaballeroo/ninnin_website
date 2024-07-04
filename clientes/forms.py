from django import forms
from .models import Cliente, Reserva, CarritoItem, Producto


class UserForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['user', 'nombre', 'apellido', 'fecha_nacimiento', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'email', 'telefono', 'fecha_reserva', 'hora']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+569XXXXXXXX'}),
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReservaForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['nombre'].initial = user.cliente.nombre


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CarritoItem
        fields = ['cantidad']
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']

