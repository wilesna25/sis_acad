import json
from pyexpat.errors import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import sis_acad_colegios
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


# COORDINADOR VIEWS

#Sedes
def crud_sedes(request):
    context = {}
    return render(request, 'coordinador/sedes.html', context)

class listar_sedes(ListView):
    model = Sedes

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_sedes = []
        for sede in self.get_queryset():
            data_sede = {}
            data_sede['id'] = sede.id
            data_sede['nombre'] = sede.nombre
            data_sede['direccion'] = sede.direccion
            data_sede['telefono'] = sede.telefono
            lista_sedes.append(data_sede)
        data = json.dumps(lista_sedes)
        return HttpResponse(data, 'application/json')


class crear_sedes(CreateView):
    model = Sedes
    form = SedeForm()

    def post(self, request, *args, **kwargs):
        self.form = SedeForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"Sede creada" } ', 'application/json')
        return HttpResponse('{ "status":"error creando  sede" } ', 'application/json')


class editar_sedes(UpdateView):
    model = Sedes
    form = SedeForm()

    def post(self, request, *args, **kwargs):
        sede = Sedes.objects.get(id=request.POST['id'])
        self.form = SedeForm(request.POST, instance=sede)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"Sede editada" } ', 'application/json')
        return HttpResponse('{ "status":"error editando  sede" } ', 'application/json')


class eliminar_sedes(DeleteView):
    model = Sedes

    def get_query(self, id):
        return self.model.objects.get(id=id)

    def post(self, request, *args, **kwargs):
        asignatura = self.get_query(request.POST['id'])
        asignatura.delete()
        return HttpResponse(' {"status":"registro borrado"}', 'application/json')
 
#PERIODOS ACADÉMICOS

def crud_periodos_academicos(request):
    context = {}
    return render(request, 'coordinador/periodos_academicos.html', context)

class listar_periodos_academicos(ListView):
    model = Sedes

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_sedes = []
        for sede in self.get_queryset():
            data_sede = {}
            data_sede['id'] = sede.id
            data_sede['nombre'] = sede.nombre
            data_sede['direccion'] = sede.direccion
            data_sede['telefono'] = sede.telefono
            lista_sedes.append(data_sede)
        data = json.dumps(lista_sedes)
        return HttpResponse(data, 'application/json')


class crear_periodos_academicos(CreateView):
    model = Sedes
    form = SedeForm()

    def post(self, request, *args, **kwargs):
        self.form = SedeForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')


class editar_periodos_academicos(UpdateView):
    model = Sedes
    form = SedeForm()

    def post(self, request, *args, **kwargs):
        sede = Sedes.objects.get(id=request.POST['id'])
        self.form = SedeForm(request.POST, instance=sede)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')


class eliminar_periodos_academicos(DeleteView):
    model = Sedes

    def get_query(self, id):
        return self.model.objects.get(id=id)

    def post(self, request, *args, **kwargs):
        asignatura = self.get_query(request.POST['id'])
        asignatura.delete()
        return HttpResponse('drop', 'application/json')

#DOCENTES
class listar_docentes(ListView):
    model = Docentes

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_docentes = []
        for docente in self.get_queryset():
            data_docente = {}
            print("Docente !!!!")
            print(type(docente))
            attrs = vars(docente)
            print("Atritubos docente :::::::")
            print(', '.join("%s: %s" % item for item in attrs.items()))
            print("Fin atributos.::::::::::::..")
            user = User.objects.get(id=docente.user_id)
            print("USERRRRRR :::")
            print(user)
            data_docente['id'] = user.id
            data_docente['first_name'] = user.first_name
            data_docente['last_name'] = user.last_name
            data_docente['username'] = user.username
            data_docente['dni'] = docente.dni
            data_docente['direccion'] = docente.direccion
            lista_docentes.append(data_docente)
        data = json.dumps(lista_docentes)
        return HttpResponse(data, 'application/json')

def crud_docentes(request):
    context = {'form':DocenteRegistroForm}
    return render(request, 'coordinador/docentes.html', context)


class registrar_docente(CreateView):
    model = User
    form = DocenteRegistroForm

    def post(self, request, *args, **kwargs):
        self.form = DocenteRegistroForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"docente creado" } ', 'application/json')
        else:
            err=self.form.errors
            return HttpResponse('{ "status":"error creando docente ' +err+'" } ', 'application/json')


def editar_docente(request):
    user_docente = User.objects.get(id=request.POST['docente_id'])
    user_docente.first_name = request.POST['first_name']
    user_docente.last_name = request.POST['last_name']
    user_docente.save()
    docente = Docentes.objects.get(user=user_docente)
    docente.dni = request.POST['dni']
    docente.direccion = request.POST['direccion']
    docente.save()
    return HttpResponse('{ "status":"docente editado" } ', 'application/json')


def eliminar_docente(request):
    docente = Docentes.objects.get(user=User.objects.get(id=request.POST['docente_id']))
    docente.delete()
    return HttpResponse('{ "status":"docente borrado" } ', 'application/json')

#ÁREAS
class listar_areas(ListView):
    model = AreasAsignaturas

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_areas = []
        for sede in self.get_queryset():
            data_area = {}
            data_area['id'] = sede.id
            data_area['area'] = sede.area
            data_area['descripcion'] = sede.descripcion
            lista_areas.append(data_area)
        data = json.dumps(lista_areas)
        return HttpResponse(data, 'application/json')

def crud_areas(request):
    context = {}
    return render(request, 'coordinador/areas.html', context)

class crear_area(CreateView):
    model = AreasAsignaturas
    form = AreasAsignaturasForm

    def post(self, request, *args, **kwargs):
        self.form = AreasAsignaturasForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"area creada" } ', 'application/json')
        return HttpResponse('{ "status":"areada error creando" } ', 'application/json')

class editar_area(UpdateView):
    model = AreasAsignaturas
    form = AreasAsignaturasForm

    def post(self, request, *args, **kwargs):
        self.form = AreasAsignaturasForm(request.POST)
        area = AreasAsignaturas.objects.get(id=request.POST['area_id'])
        self.form = AreasAsignaturasForm(request.POST, instance=area)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"area editada" } ', 'application/json')
        return HttpResponse('{ "status":"error editando" } ', 'application/json')

class eliminar_areas(DeleteView):
    model = AreasAsignaturas

    def get_query(self, area_id):
        return self.model.objects.get(id=area_id)

    def post(self, request, *args, **kwargs):
        area = self.get_query(request.POST['area_id'])
        area.delete()
        return HttpResponse('{ "status":"area eliminada" } ', 'application/json')

#ASIGNATURAS
def crud_asignaturas(request):
    areas = AreasAsignaturas.objects.all()
    context = { 'areas' : areas }
    return render(request, 'coordinador/asignaturas.html', context)

class listar_asignaturas(ListView):
    model = Asignaturas

    def get_queryset(self):
        return self.model.objects.all()
    
    def post(self, request, *args, **kwargs):
        lista_asignaturas = []
        for asignatura in self.get_queryset():
            data_asignatura = {}
            data_asignatura['id']=asignatura.id
            data_asignatura['asignatura']=asignatura.asignatura
            data_asignatura['descripcion']=asignatura.descripcion
            data_asignatura['area']=asignatura.area.area
            lista_asignaturas.append(data_asignatura)
        data = json.dumps(lista_asignaturas)
        return HttpResponse(data,'application/json')


class crear_asignaturas(CreateView):
    model = Asignaturas
    form = AsignaturaForm()

    def post(self, request, *args, **kwargs):
        self.form = AsignaturaForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"asignatura creada" } ','application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse('{ "status":"error creando asignatura borrado" } ', 'application/json')

class editar_asignaturas(UpdateView):
    model = Asignaturas
    form = AsignaturaForm()

    def post(self, request, *args, **kwargs):
        asignatura = Asignaturas.objects.get(id=request.POST['asignatura_id'])
        self.form = AsignaturaForm(request.POST, instance=asignatura)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"asignatura  editada" } ','application/json')
        return HttpResponse('error', 'application/json')

class eliminar_asignaturas(DeleteView):
    model = Asignaturas

    def get_query(self, asignatura_id):
        return self.model.objects.get(id=asignatura_id)

    def post(self, request, *args, **kwargs):
        asignatura = self.get_query(request.POST['asignatura_id'])
        asignatura.delete()
        return HttpResponse('{ "status":"asignatura borrada" } ' , 'application/json')



#Clases
def crud_clases(request):
    grupos = Grupos.objects.all()
    asignaturas = Asignaturas.objects.all()
    docentes = Docentes.objects.all()
    context = {
        'grupos':grupos,
        'asignaturas':asignaturas,
        'docentes':docentes
    }
    return render(request, 'coordinador/clases.html', context)


class listar_clases(ListView):
    model = Clases

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_clases = []
        for clase in self.get_queryset():
            data_asignatura = {}
            data_asignatura['id'] = clase.id
            data_asignatura['clase'] = clase.clase
            data_asignatura['grupo'] = clase.grupo.grupo
            data_asignatura['asignatura'] = clase.asignatura.asignatura
            data_asignatura['docente'] = clase.docente.user.id
            lista_clases.append(data_asignatura)
        data = json.dumps(lista_clases)
        return HttpResponse(data, 'application/json')

class crear_clases(CreateView):
    model = Clases
    form = ClasesForm()

    def post(self, request, *args, **kwargs):
        self.form = ClasesForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"clase creada" } ', 'application/json')
        else:
            err = self.form.errors
            print(err)
            return HttpResponse('{ "status":"clase error" } ', 'application/json')


def editar_clases(request):
    clase = Clases.objects.get(id=request.POST['clase_id'])
    clase.clase = request.POST['clase']
    clase.grupo = Grupos.objects.get(id=request.POST['grupo'])
    clase.asignatura = Asignaturas.objects.get(id=request.POST['asignatura'])
    clase.docente.user = User.objects.get(id=request.POST['docente'])
    clase.save()
    return HttpResponse('{ "status":"clase editada" } ', 'application/json')

def eliminar_clases(request):
    clase = Clases.objects.get(id=request.POST['clase_id'])
    clase.delete()
    return HttpResponse('{ "status":"clase eliminada" } ', 'application/json')


#ESTUDIANTES
def crud_estudiantes(request):
    context = {}
    return render(request, 'coordinador/estudiantes.html', context)


#Grupos
def crud_grupos(request):
    grados = GradosAcademicos.objects.all()
    docentes = Docentes.objects.all()
    sedes = Sedes.objects.all()
    jornadas = Jornadas.objects.all()
    context = {'grados':grados,
               'docentes':docentes,
               'sedes':sedes,
               'jornadas':jornadas
            }
    return render(request, 'coordinador/grupos.html', context)


class listar_grupos(ListView):
    model = Grupos

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_grupos = []
        for grupo in self.get_queryset():
            print("gRUPOOOO !!")
            data_grupo = {}
            print(grupo)
            data_grupo['id'] = grupo.id
            data_grupo['grupo'] = grupo.grupo
            data_grupo['grado'] = grupo.grado.grado
            data_grupo['docente'] = grupo.docente.user.first_name
            data_grupo['jornada'] = grupo.jornada.jornada
            data_grupo['sede'] = grupo.sede.nombre
            lista_grupos.append(data_grupo)
        data = json.dumps(lista_grupos)
        return HttpResponse(data, 'application/json')


class crear_grupos(CreateView):
    model = Grupos
    form = GruposForm()

    def post(self, request, *args, **kwargs):
        self.form = GruposForm(request.POST)
        print(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('{ "status":"grupo creado" }','application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse({ "status":"error " }, 'application/json')

class eliminar_grupos(DeleteView):
    model = Grupos

    def get_query(self, area_id):
        return self.model.objects.get(id=area_id)

    def post(self, request, *args, **kwargs):
        area = self.get_query(request.POST['grupo_id'])
        area.delete()
        return HttpResponse('{ "status":"grupo eliminado" } ', 'application/json')

def editar_grupos(request):
    grupo =  Grupos.objects.get(id=request.POST['grupo_id'])
    grupo.grupo = request.POST['grupo']
    grupo.grado = GradosAcademicos.objects.get(id=request.POST['grado'])
    #grupo.docente = (Docente) User.objects.get(id=request.POST['docente'])
    grupo.jornada = Jornadas.objects.get(id=request.POST['jornada'])
    grupo.sede = Sedes.objects.get(id=request.POST['sede'])
    grupo.save()
    return HttpResponse('{ "status":"grupo editado" } ','application/json')

#Matrículas
def crud_matriculas(request):
    grupos = Grupos.objects.all()
    context = {
               'form':MatricularEstudianteForm,
               'grupos':grupos,
            }
    return render(request, 'coordinador/matriculas.html', context)

class listar_matriculas(ListView):
    model = Estudiantes

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_matriculas = []
        for estudiante in self.get_queryset():
            data_matricula = {}
            data_matricula['id'] = estudiante.id
            data_matricula['codigo_estudiante'] = estudiante.cod_estudiante
            data_matricula['nid'] = estudiante.dni
            data_matricula['nombres'] = estudiante.nombres
            data_matricula['apellidos'] = estudiante.apellidos
            data_matricula['fecha_nacimiento'] = estudiante.fecha_nacimiento.__str__()
            data_matricula['direccion'] = estudiante.direccion
            data_matricula['telefono'] = estudiante.telefono
            data_matricula['correo'] = estudiante.correo
            data_matricula['grupo'] = Matriculas.objects.get(estudiante=estudiante).grupo.grupo
            lista_matriculas.append(data_matricula)
        data = json.dumps(lista_matriculas)
        return HttpResponse(data, 'application/json')

class crear_matriculas(CreateView):
    model = Estudiantes
    form = MatricularEstudianteForm

    def post(self, request, *args, **kwargs):
        self.form = MatricularEstudianteForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('estudiante creado', 'application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse(err, 'application/json')


def editar_matriculas(request):
    estudiante = Estudiantes.objects.get(id=request.POST['id'])
    estudiante.cod_estudiante = request.POST['cod_estudiante']
    estudiante.nombres = request.POST['nombres']
    estudiante.apellidos = request.POST['apellidos']
    estudiante.fecha_nacimiento = request.POST['fecha_nacimiento']
    estudiante.direccion = request.POST['direccion']
    estudiante.telefono = request.POST['telefono']
    estudiante.correo = request.POST['correo']
    estudiante.save()
    #crea matrícula
    matricula = Matriculas.objects.get(estudiante=estudiante)
    matricula.grupo = Grupos.objects.get(id=request.POST['grupo'])
    matricula.save()
    #crear Estudiante_por_Grupo
    est_x_grupo = Estudiantes_por_Grupo.objects.create(estudiante=estudiante, grupo=matricula.grupo)
    est_x_grupo.save()
    return HttpResponse('{ "status":"estudiante editado" } ','application/json')



def eliminar_matriculas(request):
    estudiante = Estudiantes.objects.get(id=request.POST['estudiante_id'])
    estudiante.delete()
    return HttpResponse('{ "status":"estudiante borrado" } ','application/json')







def editar_grupos(request):
    grupo =  Grupos.objects.get(id=request.POST['grupo_id'])
    grupo.grupo = request.POST['grupo']
    grupo.grado = GradosAcademicos.objects.get(id=request.POST['grado'])
    #grupo.docente = (Docente) User.objects.get(id=request.POST['docente'])
    grupo.jornada = Jornadas.objects.get(id=request.POST['jornada'])
    grupo.sede = Sedes.objects.get(id=request.POST['sede'])
    grupo.save()
    return HttpResponse('{ "status":"grupo editado" } ','application/json')

#
#DOCENTES VIEWS
#

#ASISTENCIAS
def crud_asistencia(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/asistencia.html', context)


def ver_asistencias(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/ver_asistencias.html', context)


class listar_asistencias_estudiantes(ListView):
    model = Estudiantes

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        lista_estudiantes = []
        for clase in self.get_queryset():
            data_estudiante = {}
            data_estudiante['id'] = clase.id
            data_estudiante['clase'] = clase.clase
            data_estudiante['grupo'] = clase.grupo.grupo
            data_estudiante['asignatura'] = clase.asignatura.asignatura
            data_estudiante['docente'] = clase.docente.user.id
            lista_estudiantes.append(data_estudiante)
        data = json.dumps(lista_estudiantes)
        return HttpResponse(data, 'application/json')

#BOLETIN
def ver_boletin(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/boletin.html', context)



def mostrar_boletin_estudiante(request):
    estudiante_codigo = request.POST['estudiante_codigo']
    estudiante = Estudiantes.objects.get(cod_estudiante=estudiante_codigo)
    matricula = obtener_estudiante_matricula(estudiante)
    grupo = matricula.grupo
    sede = grupo.sede.nombre
    grado = grupo.grado.grado
    jornada = grupo.jornada.jornada
    calificaciones = obtener_clases_calificadas_por_estudiante(estudiante, grupo.grado)

    
    conceptosAcademicos = _obtener_conceptos_academicos(grupo.grado, estudiante)

    #print(calificaciones[0]['area_asignatura'])
    context = {
        'estudiante_nombre': estudiante.apellidos + "  " + estudiante.nombres,
        'estudiante_jornada': jornada,
        'estudiante_grado' : grado,
        'estudiante_sede' : sede.upper(),
        'calificaciones' : calificaciones,
        'conceptosAcademicos' : conceptosAcademicos
    }
    return render(request, 'docente/boletin_estudiante.html', context)



def _obtener_conceptos_academicos(grado, estudiante):
    conceptosAcademicos = []
    clases_calificadas = Calificaciones.objects.filter(estudiante=estudiante)
    print("calificacionessss ")
    for calificada in clases_calificadas:
        conceptosAcademicosAsignatura = {}
        conceptosAcademicosAsignatura['asignatura'] = calificada.clase.asignatura.asignatura
        conceptosAcademicosAsignatura['calificacion'] = calificada.calificacion
        conceptosAcademicosAsignatura['nivelDesempeno'] = calificada.nivel_desempeno
        conceptosAcademicosAsignatura['conceptosAcademicos'] = obtener_conceptos_academicos(grado, calificada.clase.asignatura)
        #concepto_academico = obtener_conceptos_academicos(grado, calificada.clase.asignatura)
        conceptosAcademicos.append(conceptosAcademicosAsignatura)
    
    return conceptosAcademicos



def obtener_fallas_asistencias_estudiate_clase():
    pass


def obtener_clases_calificadas_por_estudiante(estudiante, grado):
    calificaciones = []
    clases_calificadas = Calificaciones.objects.filter(estudiante=estudiante)
    for calificada in clases_calificadas:
        calificacion_data = {}
        calificacion_data['area_asignatura'] = calificada.clase.asignatura.area.area + " " + calificada.clase.asignatura.asignatura
        calificacion_data['periodo'] = calificada.periodo_academico
        calificacion_data['nivel'] = calificada.nivel_desempeno
        calificacion_data['calificacion'] = calificada.calificacion
        calificacion_data['docente'] = calificada.clase.docente.last_name + " " + calificada.clase.docente.first_name
        calificacion_data['inasistencias'] = FallasAsistencias.objects.filter(estudiante=estudiante, clase=calificada.clase).count()
        #calificacion_data['logros'] = obtener_logros_x_asignatura_grado(grado, calificada.clase.asignatura, calificacion_data['nivel'] )
        calificaciones.append(calificacion_data)
    return  calificaciones


def obtener_logros_x_asignatura_grado(grado, asignatura, nivel_desempeno):
    try:
        logros = LogrosAsignaturas.objects.filter(grado=grado, asignatura=asignatura, nivel_desempeno=nivel_desempeno)
    except:
        logros = None
    return logros


def obtener_conceptos_academicos(grado, asignatura):
    # try:
    #     auxPeriodoAcademico = PeriodoAcademico.objects.filter(periodo='PRIMER_PERIODO_ACADEMICO')
    #     conceptosAcademicos = ConceptosAcademicos.objects.filter(grado=grado, asignatura=asignatura, periodo_academico=auxPeriodoAcademico)
    #     print("WOOOOORKKSSS")
    # except:
    #     print("ERROOOOOOOOOR")
    #     conceptosAcademicos = None
    auxPeriodoAcademico = PeriodoAcademico.objects.get(periodo='PRIMER_PERIODO_ACADEMICO')
    print("auxPeriodoAcademico")
    print(auxPeriodoAcademico.periodo)
    print("auxPeriodoAcademico 2")
    conceptosAcademicos = ConceptosAcademicos.objects.filter(grado_academico=grado, asignaturas=asignatura, periodo_academico=auxPeriodoAcademico)
    # print("conceptoAcademico = ")
    # print(conceptosAcademicos[0].concepto_academico)
    # print("fin conceptoAcademico")
    # print("")
    
    return conceptosAcademicos


def obtener_calificacion_area_asignatura():
    pass

def obtener_calificacion_p1(estudiante):
    calificaciones = Calificaciones.objects.get(estudiante=estudiante)
    pass

def obtener_calificacion_p2():
    pass

def obtener_calificacion_p3():
    pass

def obtener_calificacion_p4():
    pass

def obtener_calificacion_p5():
    pass

def obtener_estudiante_calificaciones(estudiante):
    calificaciones = Calificaciones.objects.filter(estudiante=estudiante)
    return calificaciones

def obtener_estudiante_matricula(estudiante):
    matricula = Matriculas.objects.get(estudiante=estudiante)
    return matricula




def ver_boletin_estudiante(request):
    context = {}
    return render(request, 'docente/boletin_estudiante.html', context)



#CALIFICACIONES
def crud_calificaciones(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/calificaciones.html', context)

def ver_calificaciones(request):

    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/ver_calificaciones.html', context)

#
#ESTUDIANTES VIEWS
#

class listar_estudiantes_x_clase(ListView):
    model = Estudiantes_por_Grupo

    def get_queryset(self, grupo_clase):
        return self.model.objects.filter(grupo=grupo_clase)


    def get_grupo_clase(self,clase):
        grupo = clase.grupo
        return grupo

    def post(self, request, *args, **kwargs):
        try:
            clase = Clases.objects.get(id=request.POST['clase_id'])
            grupo_clase = self.get_grupo_clase(clase)
            lista_estudiantes = []
            for estudiante_x_grupo in self.get_queryset(grupo_clase):
                data_estudiante = {}
                data_estudiante['id'] = estudiante_x_grupo.id
                data_estudiante['cod_estudiante'] = estudiante_x_grupo.estudiante.cod_estudiante
                data_estudiante['nombres'] = estudiante_x_grupo.estudiante.nombres
                data_estudiante['apellidos'] = estudiante_x_grupo.estudiante.apellidos
                lista_estudiantes.append(data_estudiante)
            data = json.dumps(lista_estudiantes)
            return HttpResponse(data, 'application/json')
        except:
            return HttpResponse('listar_estudiantes_x_clase no data', 'application/json')



def ver_calificaciones_estudiante(request):
    context = {}
    return render(request, 'estudiante/calificaciones.html', context)


def guardar_falla_asistencia(request):
    try:
        justificada = False
        codigo_estudiante = request.POST['codigo_estudiante']
        clase_id = request.POST['clase']
        observaciones = request.POST['observaciones']
        es_justificada = request.POST['es_justificada']
        if(es_justificada=='1'):
            justificada = True
        print("Heeere")
        fallaasistencias = FallasAsistencias.objects.create(
                estudiante=Estudiantes.objects.get(cod_estudiante=codigo_estudiante),
                clase=Clases.objects.get(id=clase_id),
                justificada=justificada,
                observaciones=observaciones
        )
        fallaasistencias.save()
        return HttpResponse("falla guardada", 'application/json')
    except:
        return HttpResponse("error", 'application/json')




def listar_fallas_asistencia_por_clase(request):
    try:
        lista_fallas_asistencias = []
        clase = Clases.objects.get(id=request.POST['clase_id'])
        fallasasistencia_x_clase=FallasAsistencias.objects.filter(clase=clase)
        for fallaasistencia in fallasasistencia_x_clase:
            falla_asistencia = {}
            falla_asistencia['clase'] = fallaasistencia.clase.clase
            falla_asistencia['fecha'] = fallaasistencia.fecha.isoformat()
            falla_asistencia['codigo_estudiante'] = fallaasistencia.estudiante.cod_estudiante
            falla_asistencia['apellidos_estudiante'] = fallaasistencia.estudiante.apellidos
            falla_asistencia['nombres_estudiante'] = fallaasistencia.estudiante.nombres
            falla_asistencia['es_justificada'] = fallaasistencia.justificada
            lista_fallas_asistencias.append(falla_asistencia)
        data = json.dumps(lista_fallas_asistencias)
        return HttpResponse(data, 'application/json')
    except:
        return HttpResponse("unexpected error", 'application/json')


def guardar_calificacion(request):
    try:
        estudiante = Estudiantes.objects.get(cod_estudiante=request.POST['estudiante_codigo'])
        clase = Clases.objects.get(id=request.POST['clase'])
        periodo_academico = int(request.POST['periodo_academico'])
        calificacion = float(request.POST['calificacion'])
        nivel_desempeno = obtener_nivel_desempeno_calificacion(float(request.POST['calificacion']))
        #Registra Nota
        calificacion = Calificaciones.objects.create(estudiante=estudiante, clase=clase, periodo_academico=periodo_academico,
                                                     calificacion=calificacion, nivel_desempeno=nivel_desempeno)
        calificacion.save()
        return HttpResponse("calificacion guardada", 'application/json')
    except:
        return HttpResponse("error", 'application/json')

def obtener_nivel_desempeno_calificacion(calificacion):
    nivel = 'SUPERIOR'
    if calificacion <=2.9:
        nivel = 'BAJO'
    elif    calificacion >= 3 and calificacion <= 3.9:
        nivel = 'BASICO'
    elif    calificacion >= 4 and calificacion <=4.5:
        nivel = 'ALTO'
    return nivel

def listar_calificaciones_x_clase(request):
    try:
        lista_calificaciones = []
        clase = Clases.objects.get(id=request.POST['clase'])
        calificaciones = Calificaciones.objects.filter(clase=clase)
        for calificacion in calificaciones:
            calificaciones_data = {}
            calificaciones_data['codigo_estudiante'] = calificacion.estudiante.cod_estudiante
            calificaciones_data['estudiante'] = calificacion.estudiante.apellidos + " " + calificacion.estudiante.nombres
            calificaciones_data['grupo'] = calificacion.clase.grupo.grupo
            calificaciones_data['asignatura'] = calificacion.clase.asignatura.asignatura
            calificaciones_data['periodo'] = calificacion.periodo_academico
            calificaciones_data['calificacion'] = calificacion.calificacion
            calificaciones_data['nivel'] = calificacion.nivel_desempeno
            lista_calificaciones.append(calificaciones_data)
        data = json.dumps(lista_calificaciones)
        return HttpResponse(data, 'application/json')
    except:
        return HttpResponse("unexpected error", 'application/json')

def cerrar_sesion(request):
    print("cerrando sesion....................")
    logout(request)
    return redirect("login")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                print("You are now logged in as {username}")
                return redirect('crud_calificaciones')
            else:
                #messages.error(request, "Invalid username or password.")
                print("Invalid username or password.")
                return HttpResponse("auth " + username + " pass : " + password, 'application/json')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})


# def login_page(request):
    
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")


#         user = authenticate(request, username=username, password=password, email=username)
#         print("autenticandooooooooooooooooo")
#         if user is not None:
#             login(request, user)
#             return redirect('crud_calificaciones')
#         else:
#             return HttpResponse("auth " + username + " pass : " + password, 'application/json')
            
    # return render(
    #     request,
    #     "login.html"
    # )