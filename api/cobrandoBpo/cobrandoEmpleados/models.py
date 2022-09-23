from django.db import models

# Creamos el modelo para departamentos.

class Departamentos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

#Creamos el modelo para empleados

class Empleados(models.Model):
    codigo = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=30)
    nombre = models.CharField(max_length=200)
    apellido1 = models.CharField(max_length=200)
    apellido2 = models.CharField(max_length=200)
    codigo_departamento = models.ForeignKey(Departamentos, null=True, blank=True, on_delete=models.CASCADE)
    