from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', views.index, name='index'),
    path('comidas/', views.comidas, name='comidas'),
    path('promociones/', views.promociones, name='promociones'),
    path('reservacion/', views.reservacion, name='reservacion'),
    path('sucursal/', views.sucursal, name='sucursal'),

    path('accounts/', include("django.contrib.auth.urls")),

    

]