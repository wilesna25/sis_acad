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
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')


class editar_sedes(UpdateView):
    model = Sedes
    form = SedeForm()

    def post(self, request, *args, **kwargs):
        sede = Sedes.objects.get(id=request.POST['id'])
        self.form = SedeForm(request.POST, instance=sede)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')


class eliminar_sedes(DeleteView):
    model = Sedes

    def get_query(self, id):
        return self.model.objects.get(id=id)

    def post(self, request, *args, **kwargs):
        asignatura = self.get_query(request.POST['id'])
        asignatura.delete()
        return HttpResponse('drop', 'application/json')

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
        print(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('docente creado', 'application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse('error: '+err, 'application/json')


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
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')

class editar_area(UpdateView):
    model = AreasAsignaturas
    form = AreasAsignaturasForm

    def post(self, request, *args, **kwargs):
        self.form = AreasAsignaturasForm(request.POST)
        area = AreasAsignaturas.objects.get(id=request.POST['area_id'])
        self.form = AreasAsignaturasForm(request.POST, instance=area)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('done', 'application/json')
        return HttpResponse('error', 'application/json')

class eliminar_areas(DeleteView):
    model = AreasAsignaturas

    def get_query(self, area_id):
        return self.model.objects.get(id=area_id)

    def post(self, request, *args, **kwargs):
        area = self.get_query(request.POST['area_id'])
        area.delete()
        return HttpResponse('drop', 'application/json')

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
            return HttpResponse('done','application/json')
        else:
            err=self.form.errors
            print(err)
            return HttpResponse(': '+err, 'application/json')

class editar_asignaturas(UpdateView):
    model = Asignaturas
    form = AsignaturaForm()

    def post(self, request, *args, **kwargs):
        asignatura = Asignaturas.objects.get(id=request.POST['asignatura_id'])
        self.form = AsignaturaForm(request.POST, instance=asignatura)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse('done','application/json')
        return HttpResponse('error', 'application/json')

class eliminar_asignaturas(DeleteView):
    model = Asignaturas

    def get_query(self, asignatura_id):
        return self.model.objects.get(id=asignatura_id)

    def post(self, request, *args, **kwargs):
        asignatura = self.get_query(request.POST['asignatura_id'])
        asignatura.delete()
        return HttpResponse('drop', 'application/json')



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





