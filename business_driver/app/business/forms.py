# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets
from .models import *
from .forms import *
from django.contrib.auth.forms import User


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=40, help_text="El texto no deve contener espacios Ejem. juan",
                               label="Nombre de Usuario")
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Confirmar")
    first_name = forms.CharField(max_length=140, label="Nombre y Apellido")
    email = forms.EmailField(label='Correo Elec.')

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "email")
        widgets = {
            'password1': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        if commit:
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False
            user.save()
        return user


class NegocioForm(forms.ModelForm):
    """FORMNAME definition."""
    class Meta:
        model = Negocio
        exclude = ('estado','mision','vision','pais','user','plan_basic','plan_premiun',)
    
    def clean_nombre_negocio(self):
        negocio = self.cleaned_data['nombre_negocio']
        if Negocio.objects.filter(nombre_negocio = negocio).exists():
            raise forms.ValidationError('Escriba un nombre más descriptivo')
        return negocio

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        exclude = ('estado','negocio',)
            

class PedidosForm(forms.ModelForm):
    """FORMNAME definition."""
    #colores = (("Rojo", "Rojo"),("Azul", "Azul"),("Amarillo", "Amarillo"),("Verde", "Verde"),)
    #tam = (("Grande", "Grande"),("Pequeño", "Pequeño"),("Cualquiera", "Cualquiera"),("Consultar", "Consultar"),)
    #color = forms.ChoiceField(choices=colores)
    #tamanio = forms.ChoiceField(choices=tam)
    class Meta:
        model = Pedido
        exclude = ('estado','catalogo',)