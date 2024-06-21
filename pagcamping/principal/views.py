from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from .forms import CustomUserCreationForm

# Create your views here.

def inicio(request):
    return render(request, 'index.html')
@login_required
def perfil(request):
    return render(request, 'registration/perfil.html')
def nosotros(request):
    return render(request, 'nosotros.html')

def vertienda(request):
    return render(request, 'tienda.html')

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