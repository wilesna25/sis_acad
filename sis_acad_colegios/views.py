import json
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

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
            return HttpResponse('done', 'application/json')
        else:
            err = self.form.errors
            print(err)
            return HttpResponse(err, 'application/json')

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
            return HttpResponse('done','application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse(err, 'application/json')



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
        print(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('estudiante creado', 'application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse(err, 'application/json')


#
#DOCENTES VIEWS
#

#ASISTENCIAS
def crud_asistencia(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(user_id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/asistencia.html', context)


def ver_asistencias(request):
    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(user_id=request.user.id))
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
        clases = Clases.objects.filter(docente=Docentes.objects.get(user_id=request.user.id))
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
    #print(calificaciones[0]['area_asignatura'])
    context = {
        'estudiante_nombre': estudiante.apellidos + "  " + estudiante.nombres,
        'estudiante_jornada': jornada,
        'estudiante_grado' : grado,
        'estudiante_sede' : sede,
        'calificaciones' : calificaciones
    }
    return render(request, 'docente/boletin_estudiante.html', context)



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
        calificacion_data['docente'] = calificada.clase.docente.user.last_name + " " + calificada.clase.docente.user.first_name
        calificacion_data['inasistencias'] = FallasAsistencias.objects.filter(estudiante=estudiante, clase=calificada.clase).count()
        calificacion_data['logros'] = obtener_logros_x_asignatura_grado(grado, calificada.clase.asignatura, calificacion_data['nivel'] )
        calificaciones.append(calificacion_data)
    return  calificaciones


def obtener_logros_x_asignatura_grado(grado, asignatura, nivel_desempeno):
    try:
        logros = LogrosAsignaturas.objects.filter(grado=grado, asignatura=asignatura, nivel_desempeno=nivel_desempeno)
    except:
        logros = None
    return logros


def obtener_calificaciones(estudiante):
    calificaciones = []
    calificacion_data = {}
    #calificacion_data['area_asignatura']
    pass

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
        clases = Clases.objects.filter(docente=Docentes.objects.get(user_id=request.user.id))
    except:
        clases = None
    context = {
        'clases' : clases
    }
    return render(request, 'docente/calificaciones.html', context)

def ver_calificaciones(request):

    try:
        clases = Clases.objects.filter(docente=Docentes.objects.get(user_id=request.user.id))
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
    nivel = 'Superior'
    if calificacion <=2.9:
        nivel = 'Bajo'
    elif    calificacion >= 3 and calificacion <= 3.9:
        nivel = 'Basico'
    elif    calificacion >= 4 and calificacion <=4.5:
        nivel = 'Alto'
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
