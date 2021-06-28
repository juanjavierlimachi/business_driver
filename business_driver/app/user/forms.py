#encoding:utf-8
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import User
from .models import *

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, label="Nombre Completo")
    class Meta:
        model = get_user_model()
        fields = ('first_name','email', 'password1', 'password2')
    def clean_first(self):
        if self.cleaned_data['first_name'] == "":
            raise forms.ValidationError('Escriba su nombre')

    def save(self,commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.username=self.cleaned_data.get("email")
        if commit:
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False
            user.save()
        return user 


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email:')


class perfil_form(forms.ModelForm):
    """FORMNAME definition."""
    celular = forms.IntegerField(label='Celular (Whatsapp)')
    class Meta:
        model = ClientePerfil
        fields = ['celular']
