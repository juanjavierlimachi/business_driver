#encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import User

class CustomUser(AbstractUser):
    email = models.EmailField(_('Correo Electrónico'), unique=True)


class ClientePerfil(models.Model):
    """Model definition for ClientePerfil."""
    usuario = models.OneToOneField(CustomUser, unique=True, related_name='perfil', on_delete = models.CASCADE)
    celular = models.PositiveIntegerField(unique=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for ClientePerfil."""

        verbose_name = 'ClientePerfil'
        verbose_name_plural = 'ClientePerfils'

    def __str__(self):
        """Unicode representation of ClientePerfil."""
        return "%s"%(self.celular)


class Servicio(models.Model):
    """Model definition for Servicio  ."""
    nombre_servicio = models.CharField('Nombre del servicio', max_length=50,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Servicio   ."""

        verbose_name = 'Categoria  '
        verbose_name_plural = 'Servicio'
    
    def __str__(self):
        """Unicode representation of Servicio ."""
        return self.nombre_servicio