from django.urls import path
from .views import (
    registrar_cliente, registrar_coche, registrar_servicio,
    buscar_cliente, buscar_coche_por_matricula,
    buscar_coches_de_cliente, lista_clientes, lista_coches, lista_servicios, lista_coche_servicios, detalle_cliente, servicios_de_coche, contacto, nuevo_cliente, nuevo_coche, nuevo_servicio,   nuevo_coche_servicio, servicios_de_coche
)
urlpatterns = [
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('lista_coches/', lista_coches, name='lista_coches'),
    path('lista_servicios/', lista_servicios, name='lista_servicios'),
    path('lista_coche_servicios/', lista_coche_servicios, name='lista_coche_servicios'),
    path('lista_coche_servicios/<int:coche_id>', servicios_de_coche, name='lista_coche_servicios'),
    path('detalle_cliente/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('servicios_de_coche/<int:coche_id>/', servicios_de_coche, name='servicios_de_coche'),
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    path('servicios/registrar/', registrar_servicio, name='registrar_servicio'),
    path('clientes/<int:cliente_id>/', buscar_cliente, name='buscar_cliente'),
    path('coches/matricula/<str:matricula>/', buscar_coche_por_matricula, name='buscar_coche_por_matricula'),
    path('clientes/<int:cliente_id>/coches/', buscar_coches_de_cliente, name='buscar_coches_de_cliente'),
    #path('coches/<int:coche_id>/servicios/', buscar_servicios_de_coche, name='buscar_servicios_de_coche'),
    path('contacto/', contacto, name='contacto'),
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('coches/nuevo/', nuevo_coche, name='nuevo_coche'),
    path('servicios/nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('coche_servicio/nuevo/', nuevo_coche_servicio, name='nuevo_coche_servicio'),
]