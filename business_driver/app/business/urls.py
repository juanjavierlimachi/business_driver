
from django.urls import path
from business_driver.app.business import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
