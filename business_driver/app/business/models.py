# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.text import slugify
from django.contrib.auth.forms import User
from business_driver.app.user.models import CustomUser
from business_driver.app.user.models import *
#from phone_field import PhoneField

# Create your models here.

class Categoria(models.Model):
    """Model definition for Categoria  ."""
    nombre_categoria = models.CharField('Categoria', max_length=50,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categoria   ."""

        verbose_name = 'Categoria  '
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        """Unicode representation of Categoria ."""
        return self.nombre_categoria


class Cuidad(models.Model):
    """Model definition for Cuidad."""
    cuidad = models.CharField('Ciudad', max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Cuidad."""

        verbose_name = 'Cuidad'
        verbose_name_plural = 'Cuidads'

    def __str__(self):
        """Unicode representation of Cuidad."""
        return self.cuidad


class Negocio(models.Model):
    """Model definition for Negocio."""
    nombre_negocio = models.CharField('Nombre de tu negocio', max_length=50)
    categoria=models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField(help_text='Escriba una descripción de que trata.?')
    direccion = models.CharField('Dirección ', max_length=50,help_text='Ejem. Av. Panamericana #590 Zona Sur')
    celular = models.PositiveIntegerField('Num. de Celular (WhatsApp)')
    pais = models.CharField('País', max_length=30, blank=True, null=True)
    lugar = models.ForeignKey(Cuidad, on_delete=models.CASCADE)
    mision = models.TextField('Misión', blank=True, null=True)
    vision = models.TextField('Visión', blank=True, null=True)
    imagen = models.ImageField('Imagen de portada', upload_to='img_negocios', blank=True, null=True, help_text="Opcional")
    slug = models.SlugField(editable=False, unique=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    #user = models.ForeignKey(User,on_delete=CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Negocio."""

        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        """Unicode representation of Categoria ."""
        return self.nombre_negocio

    def save(self, *args, **kwargs):
        #guardo el atributo slug + el id para cada negocio
        self.slug = slugify(self.nombre_negocio)
        super(Negocio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Negocio."""
        return ('')

    # TODO: Define custom methods here


class Catalogo(models.Model):
    """Model definition for Catalogo."""
    nombre_producto = models.CharField('Nombre del Producto', max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField('Archivo', upload_to='img_productos', blank=True, null=True, help_text="Adjunte una imagen del producto")
    negocio=models.ForeignKey(Negocio, on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Catalogo."""

        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        """Unicode representation of Catalogo."""
        return self.nombre_producto

    # TODO: Define custom methods here

class Orden(models.Model):
    """Model definition for Orden."""
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    negocio = models.ForeignKey(Negocio, on_delete = models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Orden."""

        verbose_name = 'Orden'
        verbose_name_plural = 'Ordens'

    def __str__(self):
        return "%s id %s"%(self.fecha_creacion, self.pk)



class Pedido(models.Model):
    """Model definition for Catalogo."""

    orden=models.ForeignKey(Orden, on_delete = models.CASCADE)
    producto=models.ForeignKey(Catalogo, on_delete=CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.FloatField()
    total = models.FloatField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Pedido."""

        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        """Unicode representation of Pedido."""
        return "%s, orden # %s"%(self.producto.nombre_producto, self.orden)

    # TODO: Define custom methods here