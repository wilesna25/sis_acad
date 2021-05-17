from django.shortcuts import render

# COORDINADOR VIEWS

def crud_asignaturas(request):
    context = {}
    return render(request, 'coordinador/asignaturas.html', context)


def crud_clases(request):
    context = {}
    return render(request, 'coordinador/clases.html', context)


def crud_docentes(request):
    context = {}
    return render(request, 'coordinador/docentes.html', context)


def crud_estudiantes(request):
    context = {}
    return render(request, 'coordinador/estudiantes.html', context)


def crud_grupos(request):
    context = {}
    return render(request, 'coordinador/grupos.html', context)


def crud_matriculas(request):
    context = {}
    return render(request, 'coordinador/matriculas.html', context)


def crud_periodos_academicos(request):
    context = {}
    return render(request, 'coordinador/periodos_academicos.html', context)



#
#DOCENTES VIEWS
#

def crud_asistencia(request):
    context = {}
    return render(request, 'docente/asistencia.html', context)


def crud_calificaciones(request):
    context = {}
    return render(request, 'docente/calificaciones.html', context)


#
#ESTUDIANTES VIEWS
#

def ver_calificaciones_estudiante(request):
    context = {}
    return render(request, 'estudiante/calificaciones.html', context)





