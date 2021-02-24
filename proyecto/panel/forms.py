from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class FormularioCrearUserCliente(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'apellido_paterno', 'apellido_materno')


class FormularioCrearUserSubcliente(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'apellido_paterno', 'apellido_materno', 'principal')


class FormularioEditarUserCliente(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'apellido_paterno', 'apellido_materno')


class FormularioEditarUserSubcliente(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'apellido_paterno', 'apellido_materno', 'principal')


class FormularioRegistroUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'apellido_paterno', 'apellido_materno')