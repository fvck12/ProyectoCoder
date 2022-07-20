from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from App_Coder.models import Curso

# Create your views here.
# Funcion para agregar curso nuevo
def curso(self, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)    
    curso.save()
    # Retornamos aviso al usuario del nuevo curso agregado
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>
    """)

def lista_curso(self):
    
    lista = Curso.objects.all()
    
    return render(self, "lista_cursos.html", {"lista_curso": lista})

def inicio(self):
    
    return render(self, "inicio.html")

def cursos(self):
    
    return render(self, "cursos.html")

def profesores(self):
    
    return render(self, "profesores.html")

def estudiantes(self):
    
    return render(self, "estudiantes.html")

def entregables(self):
    
    return render(self, "entregables.html")
