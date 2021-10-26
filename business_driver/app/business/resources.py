from import_export import resources
from .models import *

class CatalogoResource(resources.ModelResource):
    class Meta:
        model = Catalogo