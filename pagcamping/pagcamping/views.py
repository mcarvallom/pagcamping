from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request, 'index.html',{'usuario':request.user})






def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')




    