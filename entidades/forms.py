from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EspecialidadForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    
class DoctorForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    
    
class CitaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=100, required=True)
    last_name = forms.CharField(label="Apellido", max_length=100, required=True)

    class Meta:
        model = User
        fields = ["email","first_name","last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)