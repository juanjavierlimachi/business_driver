from business_driver.app.business.models import *
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):

    template_name = "business/index.html"

    def get_queryset(self):
        
    #si quiero enviar otra consulta
        dic = {
            'categorias':Categoria.objects.all(),
            #'usuarios':self.model.objects.all().count()
        }
        return dic
    def get_context_data(self, **kwargs):
        context = self.get_queryset()
        #print(context)
        #PUEDO AGREGAR MAS DATOS EL CONTEXTO contexto['otros']
        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, self.get_context_data())