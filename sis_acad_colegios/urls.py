from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.crud_docentes, name="crud_docentes"),
    ##
    #LOGIN - LOGOUT
    ##
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LoginView.as_view(template_name='logout.html'), name="logout"),
    #COORDINADOR PATHS
    #Sedes
    path('coordinador/sedes/', views.crud_sedes, name="crud_sedes"),
    path('coordinador/sedes/listar_sedes/', views.listar_sedes.as_view(), name="listar_sedes"),
    path('coordinador/sedes/crear_sedes/', views.crear_sedes.as_view(), name="crear_sedes"),
    path('coordinador/sedes/editar_sedes/', views.editar_sedes.as_view(), name="editar_sedes"),
    path('coordinador/sedes/eliminar_sedes/', views.eliminar_sedes.as_view(),
         name="eliminar_sedes"),
    #Docentesa
    path('coordinador/docentes/', views.crud_docentes, name="crud_docentes"),
    path('coordinador/docentes/listar_docentes/', views.listar_docentes.as_view(), name="listar_docentes"),
    path('coordinador/docentes/registrar_docente/', views.registrar_docente.as_view(), name="registrar_docente"),
    path('coordinador/docentes/editar_docente/', views.editar_docente, name="editar_docente"),
    path('coordinador/docentes/eliminar_docente/', views.eliminar_docente, name="eliminar_docente"),
    #Matrículas
    path('coordinador/matriculas/', views.crud_matriculas, name="crud_matriculas"),
    path('coordinador/matriculas/listar_matriculas/', views.listar_matriculas.as_view(), name="listar_matriculas"),
    path('coordinador/matriculas/crear_matriculas/', views.crear_matriculas.as_view(), name="crear_matriculas"),
    #Áreas asignaturas
    path('coordinador/areas/', views.crud_areas, name="crud_areas"),
    path('coordinador/areas/listar_areas/', views.listar_areas.as_view(), name="listar_areas"),
    path('coordinador/areas/crear_area/', views.crear_area.as_view(), name="crear_area"),
    path('coordinador/areas/editar_area/', views.editar_area.as_view(), name="editar_area"),
    path('coordinador/areas/eliminar_area/', views.eliminar_areas.as_view(), name="eliminar_areas"),
    #Grupos
    path('coordinador/grupos/', views.crud_grupos, name="crud_grupos"),
    path('coordinador/grupos/listar_grupos/', views.listar_grupos.as_view(), name="listar_grupos"),
    #path('coordinador/grupos/crear_grupos/', views.crear_grupos.as_view(), name="crear_grupos"),
    #path('coordinador/grupos/editar_grupos/', views.editar_grupos.as_view(), name="editar_grupos"),
   # path('coordinador/grupos/eliminar_grupos/', views.eliminar_grupos.as_view(), name="eliminar_grupos"),
    #Asignaturas
    path('coordinador/asignaturas/', views.crud_asignaturas, name="crud_asignaturas"),
    path('coordinador/asignaturas/listar_asignaturas/', views.listar_asignaturas.as_view(), name="listar_asignaturas"),
    path('coordinador/asignaturas/crear_asignatura/', views.crear_asignaturas.as_view(), name="crear_asignaturas"),
    path('coordinador/asignaturas/editar_asignatura/', views.editar_asignaturas.as_view(), name="editar_asignaturas"),
    path('coordinador/asignaturas/eliminar_asignatura/', views.eliminar_asignaturas.as_view(), name="eliminar_asignaturas"),
    #Clases
    path('coordinador/clases/', views.crud_clases, name="crud_clases"),
    path('coordinador/clases/listar_clases/', views.listar_clases.as_view(), name="listar_clases"),
    path('coordinador/clases/crear_clases/', views.crear_clases.as_view(), name="crear_clases"),
    #path('coordinador/clases/editar_clases/', views.editar_clases.as_view(), name="editar_clases"),
   # path('coordinador/clases/eliminar_clases/', views.eliminar_clases.as_view(), name="eliminar_clases"),
    #Periodos académicos
    path('coordinador/periodos_academicos/', views.crud_periodos_academicos, name="crud_periodos_academicos"),
    path('coordinador/asignaturas/listar_periodos_academicos', views.listar_periodos_academicos.as_view(), name="listar_periodos_academicos"),
    path('coordinador/asignaturas/crear_periodos_academicos/', views.crear_periodos_academicos.as_view(), name="crear_periodos_academicos"),
    path('coordinador/asignaturas/editar_periodos_academicos/', views.editar_periodos_academicos.as_view(), name="editar_periodos_academicos"),
    path('coordinador/asignaturas/eliminar_periodos_academicos/', views.eliminar_periodos_academicos.as_view(), name="eliminar_periodos_academicos"),

    #------------------------------------------------------------------------------------------------------------------------------
    #DOCENTE PATHS
    #------------------------------------------------------------------------------------------------------------------------------


    #BOLETIN
    path('docente/ver_boletin/', views.ver_boletin, name="ver_boletin"),
    path('docente/ver_boletin/listar_estudiantes_x_clase/', views.listar_estudiantes_x_clase.as_view(), name="listar_estudiantes_x_clase"),
    path('docente/ver_boletin/ver_boletin_estudiante/', views.ver_boletin_estudiante, name="ver_boletin_estudiante"),
    path('docente/ver_boletin/mostrar_boletin_estudiante/', views.mostrar_boletin_estudiante, name="mostrar_boletin_estudiante"),

    #ASISTENCIA
    path('docente/asistencias/', views.crud_asistencia, name="crud_asistencia"),
    path('docente/ver_asistencias/', views.ver_asistencias, name="ver_asistencias"),
    path('docente/ver_asistencias/listar_fallas_asistencia_por_clase/', views.listar_fallas_asistencia_por_clase, name="listar_fallas_asistencia_por_clase"),
    path('docente/asistencias/guardar_falla_asistencia/', views.guardar_falla_asistencia,
         name="guardar_falla_asistencia"),

    # CALIFICACIONES
    path('docente/calificaciones/', views.crud_calificaciones, name="crud_calificaciones"),
    path('docente/calificaciones/listar_estudiantes_x_clase/', views.listar_estudiantes_x_clase.as_view(), name="listar_estudiantes_x_clase"),
    path('docente/calificaciones/guardar_calificacion/', views.guardar_calificacion, name="guardar_calificacion"),
    path('docente/calificaciones/listar_calificaciones_x_clase/', views.listar_calificaciones_x_clase, name="listar_calificaciones_x_clase"),
    path('docente/ver_calificaciones/', views.ver_calificaciones, name="ver_calificaciones"),
    path('docente/ver_calificaciones/listar_calificaciones_x_clase/', views.listar_calificaciones_x_clase, name="listar_calificaciones_x_clase"),

    #GestionEstudiantes
    path('docente/asistencias/listar_estudiantes_x_clase/', views.listar_estudiantes_x_clase.as_view(), name="listar_estudiantes_x_clase"),

    path('coordinador/asignaturas/listar_asistencias_estudiantes', views.listar_asistencias_estudiantes.as_view(), name="listar_asistencias_estudiantes"),


    #ESTUDIANTE PATHS
    path('estudiante/', views.ver_calificaciones_estudiante, name="ver_calificaciones_estudiante")
]
