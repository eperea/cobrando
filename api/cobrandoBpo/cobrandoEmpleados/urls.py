from django.urls import  re_path as url
from cobrandoEmpleados import views


urlpatterns=[
    url(r'^departamento$', views.departamentoApi),
    url(r'^departamento/([0-9]+)$', views.departamentoApi),

    url(r'^empleado$', views.empleadoApi),
    url(r'^empleado/([0-9]+)$', views.empleadoApi)

]