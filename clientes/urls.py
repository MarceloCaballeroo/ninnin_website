from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('galeria', views.galeria, name='galeria'),
    path('crud', views.crud_clientes, name='crud'),

    path('menu', views.menu, name='menu'), 
    path('reserva/', views.reserva_Form, name='reserva'),

    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),

    path('reservaList', views.reserva_list, name='reserva_list'),
    path('reservaAdd', views.reserva_add, name='reserva_add'),
    path('reservaUpdate/<int:pk>', views.reserva_update, name='reserva_update'),
    path('reservaDel/<int:pk>', views.reserva_del, name='reserva_del'),

     path('redirect/', views.custom_redirect, name='custom_redirect'),

]


    