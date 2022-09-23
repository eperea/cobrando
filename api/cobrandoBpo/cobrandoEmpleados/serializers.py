from rest_framework import serializers
from cobrandoEmpleados.models import Departamentos, Empleados


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamentos
        fields=('codigo', 'nombre', 'presupuesto')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleados
        fields=('codigo', 'nif', 'nombre', 'apellido1', 'apellido2', 'codigo_departamento')



