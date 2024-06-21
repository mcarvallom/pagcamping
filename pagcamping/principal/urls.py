from django.urls import path
from . import views
from .views import exit, register

urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('tienda/',views.vertienda, name='tienda'),
    path('perfil/',views.perfil, name='perfil'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
