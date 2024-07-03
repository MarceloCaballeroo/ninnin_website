from django import forms
from .models import Cliente, Reserva

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
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+569XXXXXXXX'}),
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
