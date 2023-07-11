from django.http import HttpResponse
import datetime
from django.template import Template, Context

def pruebaTemplate(request):
    with open("C:/Users/feder/OneDrive/Escritorio/CoderHouse_Urano/repositorio_urano/miproyecto/plantillas/index.html") as file:
        plantilla = Template(file.read())
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def bienvenida(request):
    return HttpResponse("<html><h1>Bienvenidos!!!</h1></html>")

def DiaDeHoy(request):
    dia = datetime.datetime.now()
    respuestaDia = f"Hoy es: <br> {dia}"
    return HttpResponse(respuestaDia)

def saludoPersonal(request, nombre):
    saludo = f"Bienvenido {nombre}!"
    return HttpResponse(saludo)