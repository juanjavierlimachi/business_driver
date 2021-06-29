
from django.urls import path
from business_driver.app.business import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('register_negocio', views.RegisterNegocio.as_view(), name='register_negocio'),
    path('site/<str:slug>', views.SiteWeb.as_view(), name='site'),
    path('shear_tienda_view/', views.shearTiendaView, name='shear_tienda_view'),
    #path('register_user/', views.RegisterUser.as_view(), name='register_user'),
    path('negocios_por_categorias/<int:id_categoria>', views.negocios_por_categorias, name='negocios_por_categorias'),
]
