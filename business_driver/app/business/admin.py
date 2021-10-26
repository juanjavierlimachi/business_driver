from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Negocio)

admin.site.register(Pedido)
admin.site.register(Orden)
admin.site.register(Cuidad)
#admin.site.register(ClientePerfil)

class CatalogoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Catalogo,CatalogoAdmin)