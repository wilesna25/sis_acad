from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_docentes, name="crud_docentes"),
    #COORDINADOR PATHS
    path('coordinador/docentes/', views.crud_docentes, name="crud_docentes"),
    path('coordinador/grupos/', views.crud_grupos, name="crud_grupos"),
    path('coordinador/matriculas/', views.crud_matriculas, name="crud_matriculas"),
    path('coordinador/asignaturas/', views.crud_asignaturas, name="crud_asignaturas"),
    path('coordinador/clases/', views.crud_clases, name="crud_clases"),
    path('coordinador/periodos_academicos/', views.crud_periodos_academicos, name="crud_periodos_academicos"),

    #DOCENTE PATHS
    path('docente/asistencia/', views.crud_asistencia, name="crud_asistencia"),
    path('docente/calificaciones/', views.crud_calificaciones, name="crud_calificaciones"),

    #ESTUDIANTE PATHS
    path('estudiante/', views.ver_calificaciones_estudiante, name="ver_calificaciones_estudiante")
]

