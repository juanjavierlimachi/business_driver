
from django.urls import path
from business_driver.app.user import views
urlpatterns = [
    path('registerUser', views.RegisterUser.as_view(), name='registerUser'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logaut/', views.logaut, name='logaut'),
]