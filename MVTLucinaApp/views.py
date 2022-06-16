from django.shortcuts import render
from django.http import HttpResponse

from MVTLucinaApp.models import *

# Create your views here.

def inicio(request):
    
    nombre = "Lucina"
    familiarConviviente = FamiliarConviviente.objects.all()
    familiarExtendida = FamiliarExtendida.objects.all()
    contexto = {'nombre': nombre,'familiarConviviente': familiarConviviente,'familiarExtendida': familiarExtendida}
    
    return render(request,"MVTLucinaApp/index.html",contexto)
    