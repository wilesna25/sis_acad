from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Eps)
admin.site.register(Departamentos)
admin.site.register(Grupos)
admin.site.register(Ciudades)
admin.site.register(Tipos_documentos)
admin.site.register(Estratos_sociales)
admin.site.register(Grupos_sanguineos)
admin.site.register(Tipos_poblaciones)
admin.site.register(Niveles_academicos_docentes)
admin.site.register(Asignaturas)
admin.site.register(Jornadas)
admin.site.register(Estudiantes)
admin.site.register(Matriculas)
admin.site.register(Clases)
admin.site.register(GradosAcademicos)
admin.site.register(Estudiantes_por_Grupo)
#admin.site.register(Docentes)
admin.site.register(Sedes)
admin.site.register(AreasAsignaturas)
