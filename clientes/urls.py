from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('galeria', views.galeria, name='galeria'),
    path('crud', views.crud_clientes, name='crud'),

    path('menu', views.menu, name='menu'), 

    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),

    path('reservaList', views.reserva_list, name='reserva_list'),
    path('reservaAdd', views.reserva_add, name='reserva_add'),
    path('reservaUpdate/<int:pk>', views.reserva_update, name='reserva_update'),
    path('reservaDel/<int:pk>', views.reserva_del, name='reserva_del'),

    path('redirect/', views.custom_redirect, name='custom_redirect'),
    path('carrito/', views.carrito_detail, name='carrito_detail'),
    path('carrito/add/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('carrito/confirmar/', views.confirmar_compra, name='confirmar_compra'),


    path('crud_producto/', views.producto_list, name='crud_producto'),
    path('productos/add/', views.producto_add, name='producto_add'),
    path('productos/edit/<int:pk>/', views.producto_edit, name='producto_edit'),   
    path('productos/delete/<int:pk>/', views.producto_delete, name='producto_delete'),
    path('productos/comun/', views.producto_list_usuario_comun, name='producto_list_usuario_comun'),
    

    

    


]


    