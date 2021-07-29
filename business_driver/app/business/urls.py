
from django.urls import path
from business_driver.app.business import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('register_negocio', views.RegisterNegocio.as_view(), name='register_negocio'),
    path('web-<str:slug>', views.SiteWeb.as_view(), name='site'),
    path('shear_tienda_view/', views.shearTiendaView, name='shear_tienda_view'),
    #path('register_user/', views.RegisterUser.as_view(), name='register_user'),
    path('negocios_por_categorias/<int:id_categoria>', views.negocios_por_categorias, name='negocios_por_categorias'),
    path('register_contenido/<int:id_negocio>', views.registerCatalogo, name='register_contenido'),
    path('my_sites/<int:id_user>', views.mySites, name='my_sites'),

    path('pedidos/<int:id_catalogo>', views.pedidos, name='pedidos'),
    path('realizar_pedido/<int:id_producto>', views.pedidosCliente, name='pedidosCliente'),
    path('registrar_cliente_orden/<int:id_negocio>', views.registrar_cliente, name='registrar_cliente'),
    path('realizar_pedidos/<int:id_negocio>', views.realizar_pedidos, name='realizar_pedidos'),
]
