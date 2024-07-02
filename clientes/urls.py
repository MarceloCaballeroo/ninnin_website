from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('galeria', views.galeria, name='galeria'),
    path('crud', views.crud_clientes, name='crud'),

    path('menu', views.menu, name='menu'), 
    path('reserva/', views.reserva_Form, name='reserva'),

]

