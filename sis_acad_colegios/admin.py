from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import *

admin.site.register(Grupos)
admin.site.register(Asignaturas)
admin.site.register(Jornadas)
admin.site.register(Estudiantes)
admin.site.register(Matriculas)
admin.site.register(Clases)
admin.site.register(GradosAcademicos)
admin.site.register(LogrosAsignaturas)
admin.site.register(Estudiantes_por_Grupo)
admin.site.register(Docentes,UserAdmin)
admin.site.register(Sedes)
admin.site.register(AreasAsignaturas)
admin.site.register(FallasAsistencias)
admin.site.register(Calificaciones)
admin.site.register(PeriodoAcademico)
admin.site.register(ConceptosAcademicos)

#Calificaciones periodos académicos y calificaciones finales periodos académicos 
admin.site.register(CalificacionesPeriodoAcademico)
admin.site.register(CalificacionesFinalesPeriodosAcademicos)