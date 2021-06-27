#encoding:utf-8
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, View, FormView, DeleteView
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import *
from .models import *
# Create your views here.

class IndexView(TemplateView):

    template_name = "business/index.html"

    def get_queryset(self):
        
    #si quiero enviar otra consulta
        dic = {
            'categorias':Categoria.objects.all().order_by('-id'),
            'negocios':Negocio.objects.filter(estado = True).order_by('-id')
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


class RegisterNegocio(View):
    
    def get(self, request):
        Usuario=Negocio(user=request.user)
        form = NegocioForm(instance=Usuario)
        return render(request, 'business/RegisterNegocio.html', {
            'form': form
        })

    def post(self, request):
        Usuario=Negocio(user=request.user)
        print(request.user)
        form = NegocioForm(request.POST, request.FILES,instance=Usuario)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.user_id = request.user.id
            formulario.save()
            return JsonResponse({
                    'slug':formulario.slug,
                    'status':200
                })
        else:
            return render(request, 'business/RegisterNegocio.html', {
                'form': form
            })


class SiteWeb(DetailView):
    model = Negocio
    template_name = "business/SiteWeb_negocio.html"

@csrf_exempt
def shearTiendaView(request):
    if request.method=="POST":
        print("post")
        texto=request.POST["name_tiendas"]
        busqueda=(
            Q(nombre_negocio__icontains=texto) |
            Q(descripcion__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Negocio.objects.filter(busqueda, estado=True).distinct()
        return render(request,'business/shearTiendaView.html',{'negocios':resultados})
    else:
        texto=request.GET["name_tiendas"]
        busqueda=(
            Q(nombre_negocio__icontains=texto) |
            Q(descripcion__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Negocio.objects.filter(busqueda, estado=True).distinct()
        return render(request,'business/shearTiendaView.html',{'negocios':resultados})