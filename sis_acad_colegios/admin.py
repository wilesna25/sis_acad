from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Departamentos)
admin.site.register(Grupos)
admin.site.register(Ciudades)
admin.site.register(Asignaturas)
admin.site.register(Jornadas)
admin.site.register(Estudiantes)
admin.site.register(Matriculas)
admin.site.register(Clases)
admin.site.register(GradosAcademicos)
admin.site.register(Estudiantes_por_Grupo)
admin.site.register(Docentes)
admin.site.register(Sedes)
admin.site.register(AreasAsignaturas)
admin.site.register(FallasAsistencias)
admin.site.register(Calificaciones)