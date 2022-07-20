from django.urls import path

from App_Coder.views import curso, lista_curso
from App_Coder.views import cursos, inicio, profesores, estudiantes, entregables

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-curso/', lista_curso),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]