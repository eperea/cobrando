#Importanto modelos y librerías 
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from cobrandoEmpleados.models import Departamentos, Empleados
from cobrandoEmpleados.serializers import DepartamentoSerializer, EmpleadoSerializer

# CRUD DEPARTAMENTOS

@csrf_exempt
def departamentoApi(request,id=0):
    #Obtener datos

    if request.method=='GET':
        departamentos = Departamentos.objects.all()
        departamentos_serializer = DepartamentoSerializer(departamentos, many=True)
        return JsonResponse(departamentos_serializer.data, safe=False)
    
    #Enviar datos

    elif request.method == 'POST': 
        departamento_data = JSONParser().parse(request)
        departamentos_serializer = DepartamentoSerializer(data=departamento_data)
        if departamentos_serializer.is_valid():
            departamentos_serializer.save()
            return JsonResponse("Registro agregado correctamente", safe=False)
        return JsonResponse("Error al agregar registros", safe=False)

     #Actualizar datos

    elif request.method=='PUT':
        departamento_data = JSONParser().parse(request)
        departamento = Departamentos.objects.get(codigo=departamento_data['codigo'])
        departamentos_serializer=DepartamentoSerializer(departamento, data=departamento_data)
        if departamentos_serializer.is_valid():
            departamentos_serializer.save()
            return JsonResponse("Actualización exitosa", safe=False)
        return JsonResponse("Error al actualizar el registro")

    elif request.method == 'DELETE':
        departamento=Departamentos.objects.get(codigo=id)
        departamento.delete()
        return JsonResponse("El registro de borró satisfatoriamente", safe=False)


#CRUD EMPLEADOS

@csrf_exempt
def empleadoApi(request,id=0):
    #Obtener datos

    if request.method=='GET':
        empleados = Empleados.objects.all()
        empleados_serializer = EmpleadoSerializer(empleados, many=True)
        return JsonResponse(empleados_serializer.data, safe=False)
    
    #Enviar datos

    elif request.method == 'POST': 
        empleado_data = JSONParser().parse(request)
        empleados_serializer = EmpleadoSerializer(data=empleado_data)
        if empleados_serializer.is_valid():
            empleados_serializer.save()
            return JsonResponse("Registro agregado correctamente", safe=False)
        return JsonResponse("Error al agregar registros", safe=False)

     #Actualizar datos

    elif request.method=='PUT':
        empleado_data = JSONParser().parse(request)
        empleado = Empleados.objects.get(codigo=empleado_data['codigo'])
        empleados_serializer=EmpleadoSerializer(empleado, data=empleado_data)
        if empleados_serializer.is_valid():
            empleados_serializer.save()
            return JsonResponse("Actualización exitosa", safe=False)
        return JsonResponse("Error al actualizar el registro")

    elif request.method == 'DELETE':
        empleado=Empleados.objects.get(codigo=id)
        empleado.delete()
        return JsonResponse("El registro de borró satisfatoriamente", safe=False)



