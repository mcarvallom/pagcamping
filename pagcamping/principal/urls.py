from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name='inicio'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('tienda/',views.vertienda, name='tienda')

]