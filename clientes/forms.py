from django import forms
from .models import Cliente

class UserForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['user', 'nombre', 'apellido', 'fecha_nacimiento', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }