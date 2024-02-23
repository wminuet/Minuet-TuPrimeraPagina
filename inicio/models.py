from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    sector= models.CharField(max_length=40)
    puesto= models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.puesto}"