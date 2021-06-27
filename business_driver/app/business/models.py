# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.text import slugify
from django.contrib.auth.forms import User
from business_driver.app.user.models import CustomUser
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

class Negocio(models.Model):
    """Model definition for Negocio."""
    nombre_negocio = models.CharField('Nombre de tu negocio', max_length=50)
    categoria=models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField(help_text='Escriba una descripción de que trata.?')
    direccion = models.CharField('Dirección ', max_length=50,help_text='Ejem. Av. Panamericana #590 Zona Sur')
    #phone = models.PositiveIntegerField('Num. de Celular',unique=True)
    pais = models.CharField('País', max_length=30, blank=True, null=True)
    ciudad = models.CharField('Lugar', max_length=150, help_text='Pais - Ciudad')
    mision = models.TextField('Misión', blank=True, null=True)
    vision = models.TextField('Visión', blank=True, null=True)
    imagen = models.ImageField('Imagen de portada', upload_to='img_negocios', blank=True, null=True, help_text="Adjunte una imagen del producto")
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
        self.slug = slugify(self.nombre_negocio+""+str(self.pk))
        super(Negocio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Negocio."""
        return ('')

    # TODO: Define custom methods here


class Catalogo(models.Model):
    """Model definition for Catalogo."""
    nombre_producto = models.CharField('Nombre del Producto', max_length=50)
    descripción = models.TextField()
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

    def save(self):
        """Save method for Catalogo."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Catalogo."""
        return ('')

    # TODO: Define custom methods here


