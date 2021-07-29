from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Negocio)
admin.site.register(Catalogo)
admin.site.register(Pedido)
admin.site.register(Orden)
#admin.site.register(ClientePerfil)