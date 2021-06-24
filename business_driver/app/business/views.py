#encoding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, View, FormView, DeleteView
from django.db.models import Q
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
        #user_form = UserForm(instance=request.user)
        form = NegocioForm()
        return render(request, 'business/RegisterNegocio.html', {
            'form': form
        })

    def post(self, request):
        form = NegocioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponse("200")
        else:
            return render(request, 'business/RegisterNegocio.html', {
                'form': form
            })

        #messages.error(request, _('Please correct the error below.'))


""" class RegisterNegocio(FormView):
    form_class = NegocioForm
    template_name = "business/RegisterNegocio.html"
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super(RegisterNegocio, self).form_valid(form) """



class SiteWeb(DetailView):
    model = Negocio
    template_name = "business/SiteWeb_negocio.html"


def shearTiendaView(request):
    if request.method=="POST":
        texto=request.POST["name_tiendas"]
        busqueda=(
            Q(nombre_negocio__icontains=texto) |
            Q(phone_creacion__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Negocio.objects.filter(busqueda, estado=True).distinct()
        return render(request,'business/shearTiendaView.html',{'negocios':resultados})
    else:
        texto=request.GET["name_tiendas"]
        busqueda=(
            Q(nombre_negocio__icontains=texto) |
            Q(phone__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Negocio.objects.filter(busqueda, estado=True).distinct()
        return render(request,'business/shearTiendaView.html',{'negocios':resultados}) 