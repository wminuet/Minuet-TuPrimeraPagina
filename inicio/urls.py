from django.urls import path
from inicio.views import inicio, crear_empleado, empleados

urlpatterns = [
    path('', inicio, name='inicio'),
    path('empleados/', empleados, name='empleados'),
    path('empleados/nuevo/', crear_empleado, name='crear_empleado'),
]
