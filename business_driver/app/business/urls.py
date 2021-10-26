
from django.urls import path
from business_driver.app.business import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('register_negocio', views.RegisterNegocio.as_view(), name='register_negocio'),
    #path('edit_my_site/', views.EditSite.as_view(), name='edit_my_site'),
    path('web-<str:slug>', views.SiteWeb.as_view(), name='site'),
    path('shear_tienda_view/', views.shearTiendaView, name='shear_tienda_view'),
    #path('register_user/', views.RegisterUser.as_view(), name='register_user'),
    path('negocios_por_categorias/<int:id_categoria>', views.negocios_por_categorias, name='negocios_por_categorias'),
    path('negocios_por_ciudades/<int:id_ciudad>', views.negocios_por_ciudad, name='negocios_por_ciudad'),
    path('register_contenido/<int:id_negocio>', views.registerCatalogo, name='register_contenido'),
    path('my_sites/<int:id_user>', views.mySites, name='my_sites'),

    path('pedidos/<int:id_catalogo>', views.pedidos, name='pedidos'),
    path('realizar_pedido/<int:id_producto>', views.pedidosCliente, name='pedidosCliente'),#1-cuando hace click en agregar al carrito
    path('registrar_cliente_orden/<int:id_negocio>', views.registrar_cliente, name='registrar_cliente'),#2-cuando hace clik en confirmar pedido
    path('realizar_pedidos/<int:id_negocio>', views.realizar_pedidos, name='realizar_pedidos'),
    path('p-<int:id_orden>', views.pedido_online, name='pedido_online'),
    path('edit_page_web/<slug:slug>', views.EditPageWeb, name='edit_page_web'),

    path('plan_pagos/', views.PlanPagos.as_view(), name='plan_pagos'),
    path('veneficios/', views.Veneficios.as_view(), name='veneficios'),
    path('darBajaProducto/<int:id_producto>', views.darBajaProducto, name='darBajaProducto'),
    path('ver_pedidos_web/<int:id_negocio>', views.verPedidosWeb, name='ver_pedidos_web'),
    path('lista_pedidos/<int:id_orden>', views.listaPedidos, name='lista_pedidos'),
]
