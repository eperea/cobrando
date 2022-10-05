# cobrando

COBRANDO APP

Esta API REST FULL es creada con el lenguaje de programación Python, especificamente con el framework Django.

A continución explicamos como se debe consumir 

1. Instalar python la version 3.10.0 y agregar python al PATH dando check en la ventana de instalación donde esta la casilla desmarcada #enlace de descarga de Pyhton: https://www.python.org/downloads/release/python-3100/
2. Instalar Postman para probar el consumo de la API REST #Enlace de descarga: https://www.postman.com/downloads/
3. clonar el repositorio del proyecto dentro del disco C en Windows, abriendo la consola CMD ubicandose en la ruta C:\ y luego ingresar el siguiente comando: git clone https://github.com/eperea/cobrando.git
4. Instalar en modulo de Django, puede ser a través de consola ejecutando el siguiente comando: pip install django
5. Instalar el framework de Django ejecutando el siguiente comando a través de la consola: pip install djangorestframework
6. Deshabilitar el bloqueo de dominios por defecto de Django ejecuando el siguiente comando por consola: pip install django-cors-headers
7. Instalar el adaptador para postgresql con el siguiente comando a través de la consola: pip install psycopg2 #La base de datos se encuentra en un servidor remoto, los datalles de la misma se encuentran en el codigo del proyecto en la siguiente ruta: cobrandoBpo/settings.py line 85 a la 95
8. Nos ubicamos dentro de la ruta siguiente: C:\cobrando\api\cobrandoBpo (donde se encuentra el proyecto) usando la consola cmd y ejecutamos el servidor con el siguiente comando: python manage.py runserver 127.0.0.1:1234

METODOS, PARAMETROS Y RESPUESTAS TABLA DEPARTEMENTO

9. Para Obtener los registros de la tabla departamento
EJEMPLO:
-METODO: GET
-URI: 127.0.0.1:1234/departamento
-RESPUESTA: [
  {
    "codigo": 1,
    "nombre": "RRHH",
    "presupuesto": 20000000.0
  },
  {
    "codigo": 2,
    "nombre": "TI",
    "presupuesto": 20000000.0
  },
  {
    "codigo": 4,
    "nombre": "GERENCIA",
    "presupuesto": 25000000.0
  }
  ]

10. Para ingresar un nuevo registro.
EJEMPLO:
-METODO: POST
-URI: 127.0.0.1:1234/departamento
-RESPUESTA: "Registro agregado correctamente"
-EJEMPLO:    
{
        "nombre": "SERVICIO AL CLIENTE",
        "presupuesto": 25000000.0
}

11. Actualizar registro
EJEMPLO:
-METODO: PUT
-URI: 127.0.0.1:1234/departamento
-RESPUESTA: "Actualización exitosa"
-EJEMPLO:    
   {
        "codigo": 6,
        "nombre": "SERVICIO AL CLIENTE",
        "presupuesto": 15000000.0
    }
    
12. Borrar registro

Se envia el codigo del departamento a través de la URI como aparece a continuación:
EJEMPLO:
-METODO: DELETE
-URI:  127.0.0.1:1234/departamento/6
-RESPUESTA: "El registro de borró satisfatoriamente"

METODOS, PARAMETROS Y RESPUESTAS TABLA EMPLEADO

13. Para Obtener los registros de la tabla empleado
EJEMPLO:
-METODO: GET
-URI: 127.0.0.1:1234/empleado
-RESPUESTA:

[
  {
    "codigo": 1,
    "nif": "1130651803",
    "nombre": "Emmanuel",
    "apellido1": "Perea",
    "apellido2": "Cabezas",
    "codigo_departamento": 1
  },
  {
    "codigo": 2,
    "nif": "123456",
    "nombre": "Enrique",
    "apellido1": "Sanchez",
    "apellido2": "Perez",
    "codigo_departamento": 1
  }
]


14. Para ingresar un nuevo registro.
EJEMPLO:
-METODO: POST
-URI: 127.0.0.1:1234/empleado
-RESPUESTA: "Registro agregado correctamente"
-EJEMPLO:    
{
    "codigo": 3,
    "nif": "31566351",
    "nombre": "Elizabeth",
    "apellido1": "Solis",
    "apellido2": "Navas",
    "codigo_departamento": 1
  }

15. Actualizar registro
EJEMPLO:
-METODO: PUT
-URI: 127.0.0.1:1234/empleado
-RESPUESTA: "Actualización exitosa"
-EJEMPLO:    
  {
    "codigo": 4,
    "nif": "31566351",
    "nombre": "Consuelo",
    "apellido1": "Solis",
    "apellido2": "Navas",
    "codigo_departamento": 1
  }
    
16. Borrar registro

Se envia el codigo del empleado a través de la URI como aparece a continuación:
EJEMPLO:
-METODO: DELETE
-URI:  127.0.0.1:1234/empleado/2
-RESPUESTA: "El registro de borró satisfatoriamente"
