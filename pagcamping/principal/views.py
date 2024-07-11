from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .formArriendo import RentalForm
from .models import Cliente
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.dispatch import receiver
from .forms import ContactoForm
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
            messages.success(request, "Información de contacto enviada con éxito.")
            return redirect (nosotros)
        else:
            data["form"] = formularioContacto
            data['mensaje'] = "Campo email debe ser tipo hola@gmail.com"

    return render(request, 'nosotros.html', data)
def tienda(request):
    productos_disponibles = Producto.objects.filter(disponible=True)
    return render(request, 'tienda.html', {'productos': productos_disponibles})
def precios(request):
    return render(request, 'precios.html')
def exit(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito")
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
    messages.success(request, "Reserva realizada con éxito")
    # Redirigir al usuario al carrito
    return redirect('carrito')
def agregar_producto(request, id):
    producto = Producto.objects.get(id=id)

    # Verificar si existe el carrito en la sesión
    if 'carrito' not in request.session:
        request.session['carrito'] = {}

    # Verificar si el producto ya está en el carrito y si hay suficiente cantidad disponible
    if str(producto.id) in request.session['carrito'] and producto.cantidad > request.session['carrito'][str(producto.id)]:
        request.session['carrito'][str(producto.id)] += 1
    elif str(producto.id) not in request.session['carrito'] and producto.cantidad > 0:
        request.session['carrito'][str(producto.id)] = 1
    else:
        messages.error(request, 'No se pudo agregar el producto al carrito.')

    # Mensaje de éxito al agregar el producto al carrito
    messages.success(request, f'Se agregó "{producto.nombreProducto}" al carrito.')

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
    for id, cantidad in request.session['carrito'].items():
        producto = Producto.objects.get(id=id)
        productos.append((producto, cantidad))
        if cantidad > producto.cantidad:
            messages.error(request, f'No hay suficiente stock de "{producto.nombreProducto}" para completar la compra.')
            
    
    for producto, cantidad in productos:
        producto.cantidad -= cantidad
        producto.save()

    request.session['carrito'] = {}
    messages.success(request, '¡Compra realizada con éxito!')

    return redirect('carrito')
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
@login_required
def eliminarCuenta(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
        return redirect('inicio')

    return render(request, 'eliminarCuenta.html')

