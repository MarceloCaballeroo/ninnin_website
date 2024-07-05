from django import forms
from .models import Cliente, Reserva, CarritoItem, Producto
from datetime import date


class UserForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['user', 'nombre', 'apellido', 'fecha_nacimiento', 'email', 'password']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if not apellido.isalpha():
            raise forms.ValidationError("El apellido debe contener solo letras.")
        return apellido

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        today = date.today()
        edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if edad < 18:
            raise forms.ValidationError("Debe ser mayor de 18 años para registrarse.")
        return fecha_nacimiento



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

