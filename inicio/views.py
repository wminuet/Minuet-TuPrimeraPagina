from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.
def inicio(request):
    # V1
    #archivo_abierto = open(r'C:\Users\walte\Documents\Entrega_3\templates\inicio.html', 'r')
    #template = Template(archivo_abierto.read())
    #archivo_abierto.close()
    #contexto = Context()
    #template_renderizado = template.render(contexto)
    #return HttpResponse(template_renderizado)

    #v2 cargadores    
    #template = loader.get_template('inicio.html')
  
    #dicc = {
    #    'nombre': 'Carlos',
    #    'apellido': 'Perez'
    #}
    #template_renderizado = template.render(dicc)
    #return HttpResponse(template_renderizado)

    #v3 render
    dicc = {
        'nombre': 'Carlos',
        'apellido': 'Perez'
    }
    return render(request, 'inicio.html', dicc)