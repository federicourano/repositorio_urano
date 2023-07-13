from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from miapp.models import Curso

def pruebaTemplate(request):
    plantilla = loader.get_template("index.html")
    datos = {
        "Nombre": "Federico",
        "Apellido": "Urano",
        "DNI": 42933528,
        "fecha_hoy": datetime.datetime.now(),
        "notas": [7, 10, 3, 9, 6, 5, 7, 1],
    }
    documento = plantilla.render(datos)
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

def crearCurso(request, pnombre, pcomision):
    curso = Curso(nombre = pnombre, comision = pcomision)
    curso.save()
    respuesta = f"El curso creado fue {curso.nombre} de la comision {curso.comision}"
    return HttpResponse(respuesta)