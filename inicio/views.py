from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Empleado
from inicio.forms import FormularioCreacionEmpleado

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
   
    return render(request, 'inicio.html', {})

def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados':empleados})


def crear_empleado(request):
      # v2
      formulario = FormularioCreacionEmpleado()
      if request.method =="POST":
          formulario = FormularioCreacionEmpleado(request.POST)
          if formulario.is_valid():
              nombre = formulario.cleaned_data.get('nombre')
              apellido = formulario.cleaned_data.get('apellido')
              dni = formulario.cleaned_data.get('dni')
              sector = formulario.cleaned_data.get('sector')
              puesto = formulario.cleaned_data.get('puesto')
              empleado= Empleado(nombre=nombre, apellido=apellido, dni=dni,sector=sector,puesto=puesto)
              empleado.save()
              return redirect("empleados")
          
      return render(request, 'crear_empleado.html',{'formulario':formulario})
    
      # v1
      #if request.method =="POST":
      # nombre = request.POST.get('nombre')
      # apellido = request.POST.get('apellido')
      # dni = request.POST.get('dni')
      # sector = request.POST.get('sector')
      # puesto = request.POST.get('puesto')
      # empleado= Empleado(nombre=nombre, apellido=apellido, dni=dni,sector=sector,puesto=puesto)
      # empleado.save()
      # return render(request, 'crear_empleado.html',{})
   


#def crear_empleado(request, nombre, apellido, dni, sector, puesto):
#   empleado= Empleado(nombre=nombre, apellido=apellido, dni=dni,sector=sector,puesto=puesto)
#   empleado.save()
#   return render(request, 'crear_empleado.html',{'empleado':empleado})