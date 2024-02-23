from django import forms

class FormularioCreacionEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    sector = forms.CharField(max_length=40)
    puesto = forms.CharField(max_length=20)