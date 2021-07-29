#encoding:utf-8
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, View, FormView, DeleteView
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, request
from .forms import *
from .models import *
from business_driver.app.user.models import Servicio
from business_driver.app.user.forms import *
from business_driver.app.user.models import *
import json
# Create your views here.

class IndexView(TemplateView):

    template_name = "business/index.html"

    def get_queryset(self):
        
    #si quiero enviar otra consulta
        dic = {
            'categorias':Categoria.objects.all().order_by('-id'),
            'negocios':Negocio.objects.filter(estado = True).order_by('-id'),
            'servicios':Servicio.objects.filter(estado = True).order_by('-id')
            #'usuarios':self.model.objects.all().count()
        }
        return dic
    def get_context_data(self, **kwargs):
        context = self.get_queryset()
        #print(context)
        #PUEDO AGREGAR MAS DATOS EL CONTEXTO contexto['otros']
        return context

    def get(self, request, *args, **kwargs):
        request.session['compra'] = []
        print(request.session['compra'])
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
    template_name = "business/SiteWeb_negocio.html"
    es_propietario = False
    
    def get(self, request, *args, **kwargs):
        
        request.session['compra']#creo una session para los pedidos
        dato_negocio = Negocio.objects.get(slug = kwargs['slug'])
        
        if dato_negocio.user.id == request.user.id:
            self.es_propietario = True
        contex = {
            "object": dato_negocio,
            "catalogos": Catalogo.objects.filter(estado = True, negocio = dato_negocio.id).order_by('-id'),
            "es_propietario": self.es_propietario,
            "compra":len(request.session['compra'])
        }
        return render(request, self.template_name, contex)

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

def negocios_por_categorias(request, id_categoria):
    negocios = Negocio.objects.filter(estado = True, categoria = id_categoria)
    return render(request, 'business/negocios_por_categorias.html',{'negocios':negocios})

def registerCatalogo(request, id_negocio):
    dato=Negocio.objects.get(id = id_negocio)
    #print(dato)
    if request.method=='POST':
        forms=CatalogoForm(request.POST, request.FILES, instance=dato)
        if forms.is_valid():
            datos = Catalogo()
            datos.nombre_producto = request.POST['nombre_producto']
            datos.descripcion = request.POST['descripcion']
            datos.precio = float(request.POST['precio'])
            datos.imagen = request.FILES['imagen']
            datos.negocio_id = int(id_negocio)
            datos.save()
            return JsonResponse({'status':200})
    else:
        forms=CatalogoForm(instance=dato)
    return render(request,'business/registerCatalogo.html',{'form':forms,'dato':dato})

def mySites(request, id_user):
    sites = Negocio.objects.filter(user = int(id_user))

    return render(request, 'business/mySites.html',{'negocios':sites})


def pedidos(request, id_catalogo):
    if request.method=='POST':
        forms=PedidosForm(request.POST)
        if forms.is_valid():
            if Pedido.objects.filter(celular = int(request.POST['celular'])).exists():
                print('registrado')
                return HttpResponse('200')
            else:
                datos = Pedido()
                datos.nombre = request.POST['nombre']
                datos.celular = int(request.POST['celular'])
                datos.catalogo_id = int(id_catalogo)
                datos.cantidad = int(request.POST['cantidad'])
                datos.save()
                return HttpResponse('200')
        else:
            return HttpResponse('No se puedo enviar este pedido por favor revise los datos e intente nuevamente gracias.')
    else:
        form = PedidosForm()
        return render(request, 'business/pedidos.html', 
                {
                    'form':form,
                    'catalogo':Catalogo.objects.get(id=int(id_catalogo))
                    })




def pedidosCliente(request, id_producto):
    datos={}
    producto = Catalogo.objects.get(id = int(id_producto))
    data_cli = request.session['compra']
    if request.method == 'POST':
        datos['id_producto'] = int(producto.id)
        datos['nombre'] = producto.nombre_producto
        datos['cantidad'] = int(request.POST['cantidad'])
        datos['precio_uni'] = float(producto.precio)
        datos['total'] = float(int(request.POST['cantidad']) * float(producto.precio))
        data_cli.append(datos)
        request.session['compra'] = data_cli
        #print(request.session['compra'])
        return HttpResponse(len(request.session['compra']))

def registrar_cliente(request, id_negocio):
    
    if len(request.session['compra'])<=0:
        return HttpResponse('Aún no tiene nada en su compra, \n seleccione uno o más productos')
    if request.method == 'POST':
        forms=ClienteForm(request.POST)
        if forms.is_valid():
            #crear orden
            
            cliente = forms.save(commit=False)
            cliente.save()

            id_orden = crear_orden(cliente.id,id_negocio)

            realizar_pedidos(request,id_orden, id_negocio)
            #hacer el pedido
            #pedido = Pedido() registrar los pedidos con un for

            return HttpResponse('200')
    else:
        forms = ClienteForm()
    return render(request,'user/registrar_cliente.html',{'form':forms,'id_negocio':id_negocio})

def crear_orden(id_cliente, id_negocio):
    orden = Orden()
    orden.cliente_id = int(id_cliente)
    orden.negocio_id = int(id_negocio)
    orden.save()
    return orden.id

def realizar_pedidos(request,id_orden, id_negocio):
    negocio = Negocio.objects.get(id = int(id_negocio))
    dic = {
        'compras':request.session['compra'],
        'celular_negocio':negocio.celular
    }
    
    """"
    if len(request.session['compra'])<=0:
        return HttpResponse('error')
    else:
    """
    for productos in request.session['compra']:#[{'id_producto':12,'cantidad':1},{'id_producto':10,'cantidad':2}]
        print(productos)
        pedido = Pedido()
        pedido.orden_id = int(id_orden)
        pedido.producto_id = int(productos['id_producto'])
        pedido.cantidad = int(productos['cantidad'])
        pedido.precio_unitario = float(productos['precio_uni'])
        pedido.total = float(productos['total'])
        pedido.save()
        for key, value in productos.items():#{'id_producto':12,'cantidad':1}
            #print(productos[key])
            
            print(key , "-", value)
            
            

        print('···········')
    return JsonResponse(dic)