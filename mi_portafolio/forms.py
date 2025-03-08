from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import bd_1, bd_2, LoginUs, Comentario


# Clase Registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = LoginUs
        fields = ["username", "email", "password1", "password2"]

# Clase Ingreso


class LoginForm(AuthenticationForm):
    pass


# Clase Formulario1
class Formulario1(forms.ModelForm):
    class Meta:
        model = bd_1
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'})
        }


class Formulario2(forms.ModelForm):
    class Meta:
        model = bd_2
        fields = ['nombre_completo', 'cedula', 'pais', 'mensaje']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Documento'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pais Residencia'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'})
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["nombre", "mensaje"]
