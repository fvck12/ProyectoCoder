from django.urls import path

from App_Coder.views import curso, lista_curso, cursos, inicio, profesores, estudiantes, entregables

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-curso/', lista_curso),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
]