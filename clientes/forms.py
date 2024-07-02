from django import forms
from .models import Cliente , Reserva

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
        fields = "__all__"
        widgets = {
            'hora': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
