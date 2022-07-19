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