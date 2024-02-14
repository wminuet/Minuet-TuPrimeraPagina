from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

# Create your views here.
def inicio(request):
    
    archivo_abierto = open(r'C:\Users\walte\Documents\Entrega_3\templates\inicio.html', 'r')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    return HttpResponse('')