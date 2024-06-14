from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def inicio(request):
    return render(request, 'index.html')
def nosotros(request):
    return render(request, 'nosotros.html')
def vertienda(request):
    return render(request, 'tienda.html')
