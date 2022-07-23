from django.contrib import admin

from .models import Curso, Entregable, Estudiante, Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'profesion']
    search_fields = ['nombre', 'apellido']
    
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']
    search_fields = ['nombre', 'apellido']

class EntregableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fechaDeEntrega', 'entregado', 'estudiantes']
    search_fields = ['nombre', 'estudiantes']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada']
    search_fields = ['nombre', 'camada']

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)
