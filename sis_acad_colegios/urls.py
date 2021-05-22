from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_docentes, name="crud_docentes"),
    #COORDINADOR PATHS
    #Sedes
    path('coordinador/sedes/', views.crud_sedes, name="crud_sedes"),
    path('coordinador/sedes/listar_sedes/', views.listar_sedes.as_view(), name="listar_sedes"),
    path('coordinador/sedes/crear_sedes/', views.crear_sedes.as_view(), name="crear_sedes"),
    path('coordinador/sedes/editar_sedes/', views.editar_sedes.as_view(), name="editar_sedes"),
    path('coordinador/sedes/eliminar_sedes/', views.eliminar_sedes.as_view(),
         name="eliminar_sedes"),
    #Docentes
    path('coordinador/docentes/', views.crud_docentes, name="crud_docentes"),
    path('coordinado/docentes/list_docentes/', views.list_docentes, name="list_docentes"),
    
    path('coordinador/grupos/', views.crud_grupos, name="crud_grupos"),
    
    path('coordinador/matriculas/', views.crud_matriculas, name="crud_matriculas"),
    
    path('coordinador/asignaturas/', views.crud_asignaturas, name="crud_asignaturas"),
    path('coordinador/asignaturas/listar_asignaturas/', views.listar_asignaturas.as_view(), name="listar_asignaturas"),
    path('coordinador/asignaturas/crear_asignatura/', views.crear_asignaturas.as_view(), name="crear_asignaturas"),
    path('coordinador/asignaturas/editar_asignatura/', views.editar_asignaturas.as_view(), name="editar_asignaturas"),
    path('coordinador/asignaturas/eliminar_asignatura/', views.eliminar_asignaturas.as_view(), name="eliminar_asignaturas"),

    path('coordinador/clases/', views.crud_clases, name="crud_clases"),

    path('coordinador/periodos_academicos/', views.crud_periodos_academicos, name="crud_periodos_academicos"),



    #DOCENTE PATHS
    path('docente/asistencia/', views.crud_asistencia, name="crud_asistencia"),
    path('docente/calificaciones/', views.crud_calificaciones, name="crud_calificaciones"),

    #ESTUDIANTE PATHS
    path('estudiante/', views.ver_calificaciones_estudiante, name="ver_calificaciones_estudiante")
]

