from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .formArriendo import RentalForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Cliente
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import ContactoForm
from django.db.models.signals import post_save
from .models import Producto
from .forms import CustomUserChangeForm

# Create your views here.

def inicio(request):
    return render(request, 'index.html')
@login_required
def perfil(request):
    return render(request, 'registration/perfil.html')
def nosotros(request):
    data = {
        'form': ContactoForm()
    }
    if request.method== 'POST':
        formularioContacto = ContactoForm(data=request.POST)
        if formularioContacto.is_valid():
            formularioContacto.save()
            data["mensaje"] = "Información de contacto envíada con éxito."
            return redirect (nosotros)
        else:
            data["form"] = formularioContacto
            data['mensaje'] = "Formulario con errores"

    return render(request, 'nosotros.html', data)

def tienda(request):
    productos_disponibles = Producto.objects.filter(disponible=True)
    return render(request, 'tienda.html', {'productos': productos_disponibles})

def precios(request):
    return render(request, 'precios.html')
def exit(request):
    logout(request)
    return redirect('inicio')
def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')
    return render(request, 'registration/register.html', data)
def mostrarPrecios(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            arriendo = form.save(commit=False)
            # Aquí puedes asignar otros campos si es necesario, pero no asignarás un cliente
            arriendo.save()
            messages.success(request, "Reserva realizada con éxito")
            return redirect('carrito')  # Reemplaza 'carrito' con la ruta correcta hacia donde quieras redirigir
        else:
            messages.error(request, "Por favor, corrija los errores a continuación.")
    else:
        form = RentalForm()
    return render(request, 'precios.html', {'form': form})
def carrito(request):
    productos = []
    for id, cantidad in request.session["carrito"].items():
        productos.append((Producto.objects.get(id=id), cantidad))
    
    #productos = Producto.objects.filter(id__in=request.session["carrito"])
    suma_precios = sum([x[0].precio*x[1] for x in productos])
    return render(request, 'cart.html', {"productos": productos, "suma_precios":suma_precios, "carrito": request.session["carrito"]})
def guardar_reserva_y_agregar_carrito(request):
    if 'carrito' not in request.session:
        request.session['carrito'] = {}

    cant_carpas_menor4 = int(request.POST.get('cant_carpas_menor4', 0))
    cant_carpas_mayor4 = int(request.POST.get('cant_carpas_mayor4', 0))

    if cant_carpas_menor4 > 0:
        producto_id_menor4 = '10' 
        if producto_id_menor4 in request.session['carrito']:
            request.session['carrito'][producto_id_menor4] += cant_carpas_menor4
        else:
            request.session['carrito'][producto_id_menor4] = cant_carpas_menor4

    if cant_carpas_mayor4 > 0:
        producto_id_mayor4 = '11'  
        if producto_id_mayor4 in request.session['carrito']:
            request.session['carrito'][producto_id_mayor4] += cant_carpas_mayor4
        else:
            request.session['carrito'][producto_id_mayor4] = cant_carpas_mayor4

    # Guardar la sesión
    request.session.modified = True

    # Redirigir al usuario al carrito
    return redirect('carrito')
def agregar_producto(request,id):
    producto = Producto.objects.get(id=id)
    if str(producto.id) in request.session["carrito"].keys() and producto.cantidad > request.session["carrito"][str(producto.id)]:
        request.session["carrito"][str(producto.id)] += 1
    elif str(producto.id) not in request.session["carrito"].keys() and producto.cantidad > 0:
        request.session["carrito"][str(producto.id)] = 1
    else:
        pass
    return redirect('tienda')
def eliminar_producto(request, id):
    del request.session["carrito"][str(id)]
    return redirect('carrito')
def restar_producto(request, id):
    request.session["carrito"][str(id)] -=1
    if request.session["carrito"][str(id)] <= 0:
        del request.session["carrito"][str(id)]
    return redirect('carrito')
def limpiar_carrito(request):
    request.session["carrito"] = {}
    return redirect('carrito')
def comprar_carrito(request):
    productos = []
    for id, cantidad in request.session["carrito"].items():
        producto = Producto.objects.get(id=id)
        productos.append((producto, cantidad))
        if cantidad > producto.cantidad:
            return render(request, 'index.html', {"mensaje":"Error en la Compra"})
    
    for producto, cantidad in productos:
        producto.cantidad = producto.cantidad - cantidad
        producto.save()

    request.session["carrito"] = {}
    
    return render(request, 'index.html', {"mensaje":"Gracias por Comprar!!"})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado correctamente!')
            return redirect('perfil')  # Cambia 'perfil' por la URL de tu perfil actual
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'registration/editarPerfil.html', {'form': form})