from django.urls import path
from . import views
from .views import exit, register

urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('tienda/',views.tienda, name='tienda'),
    path('perfil/',views.perfil, name='perfil'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('precios/', views.mostrarPrecios, name= 'precios'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<int:id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:id>/', views.restar_producto, name='restar_producto'),
    path('vaciar/', views.limpiar_carrito, name='vaciar_carrito'),
    path('comprar/', views.comprar_carrito, name='comprar_carrito'),
    path('guardar_reserva_y_agregar_carrito/', views.guardar_reserva_y_agregar_carrito, name='guardar_reserva_y_agregar_carrito'),
    path('editarPerfil/', views.editar_perfil, name='editar_perfil'),
    path('eliminarCuenta/', views.eliminarCuenta, name='eliminarCuenta'),
]