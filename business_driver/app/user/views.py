#encoding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from business_driver.app.user.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, View, FormView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import *

from .forms import *
# Create your views here.


from django.contrib.auth import views as auth_views

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'user/login.html', {'form':form})
    """ form_class = LoginForm
    template_name = 'user/login.html' """
    def post(self, request, *args, **kwargs):
        #form = LoginForm(request.POST)
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        print ("user",user)
        if user is not None:
            login(request, user)
            
            return HttpResponse('200')
        else:
            return HttpResponse("Error los datos ingresados no son válidos, intetente nuevamente gracias.")


class RegisterUser(CreateView):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        user_perfil = perfil_form()
        return render(request, 'user/registerUser.html', {'form': form, 'user_perfil':user_perfil})
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        user_perfil = perfil_form(request.POST)
        if form.is_valid() and user_perfil.is_valid():
            user_dato = form.save()#guardo los datos del form..
            perfil = ClientePerfil()
            perfil.usuario = user_dato
            perfil.celular = request.POST['celular']
            
            perfil.save()

            user = authenticate(
                username=request.POST['email'],
                password=request.POST['password1']
            )
            if user is not None:
                login(request, user)
                print ("user",user)
                return HttpResponse("200")
        else:
            return render(request, 'user/registerUser.html', {'form': form, 'user_perfil':user_perfil})
def logaut(request):
    logout(request)
    return redirect("/")