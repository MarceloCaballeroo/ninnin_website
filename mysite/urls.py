from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),

    path('', views.index, name='index'),
    path('comidas/', views.comidas, name='comidas'),
    path('promociones/', views.promociones, name='promociones'),
    path('sucursal/', views.sucursal, name='sucursal'),

    path('accounts/', include("django.contrib.auth.urls")),
    
<<<<<<< HEAD
    
=======
>>>>>>> d11efd70ebe0de4bce8595c769bc41178bbb9990

]