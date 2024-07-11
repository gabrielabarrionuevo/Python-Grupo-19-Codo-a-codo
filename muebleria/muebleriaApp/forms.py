from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Nombre de Usuario"),
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'})
    )
    password = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
