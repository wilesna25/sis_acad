from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.db import transaction


class ClasesForm(ModelForm):
    class Meta:
        model = Clases
        fields = '__all__'

class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'

class SedeForm(ModelForm):
    class Meta:
        model = Sedes
        fields = '__all__'


class GruposForm(ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'


class AreasAsignaturasForm(ModelForm):
    class Meta:
        model = AreasAsignaturas
        fields = '__all__'


class DocenteRegistroForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    dni = forms.IntegerField(required=True)
    direccion = forms.CharField(required=True)
    username = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.password1 = 'Holamundo123'
        user.password1 = 'Holamundo123'
        user.is_teacher = True
        user.save()
        docente = Docentes.objects.create(user=user)
        docente.dni = self.cleaned_data.get('dni')
        docente.direccion = self.cleaned_data.get('direccion')
        docente.save()
        return user


class MatricularEstudianteForm(ModelForm):

    grupo = forms.IntegerField(required=True)

    class Meta:
        model = Estudiantes
        fields = '__all__'

    @transaction.atomic
    def save(self):
        #crea estudiante
        estudiante = Estudiantes.objects.create()
        estudiante.cod_estudiante = self.cleaned_data.get('cod_estudiante')
        estudiante.dni = self.cleaned_data.get('dni')
        estudiante.nombres = self.cleaned_data.get('nombres')
        estudiante.apellidos = self.cleaned_data.get('apellidos')
        estudiante.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        estudiante.direccion = self.cleaned_data.get('direccion')
        estudiante.telefono = self.cleaned_data.get('telefono')
        estudiante.correo = self.cleaned_data.get('correo')
        estudiante.save()
        #crea matr??cula
        matricula = Matriculas.objects.create(estudiante=estudiante)
        matricula.grupo = Grupos.objects.get(id=self.cleaned_data.get('grupo'))
        matricula.save()
        #crear Estudiante_por_Grupo
        est_x_grupo = Estudiantes_por_Grupo.objects.create(estudiante=estudiante, grupo=matricula.grupo)
        est_x_grupo.save()
        return estudiante


class RegistrarCalificacion():

    class Meta:
        model = Calificaciones
        fields = '__all__'

    @transaction.atomic
    def save(self):
        #Obtiene POST
        estudiante = Estudiantes.objects.get(cod_estudiante=self.cleaned_data.get('estudiante_codigo'))
        clase = Clases.objects.get(id=self.cleaned_data.get('clase'))
        periodo_academico = self.cleaned_data.get('periodo_academico')
        calificacion = self.cleaned_data.get('calificacion')
        #Registra Nota
        calificacion = Calificaciones.objects.create(estudiante=estudiante, clase=clase, periodo_academico=periodo_academico, calificacion=calificacion)
        calificacion.save()
        return calificacion


class formCalificacionesPeriodoAcademico(ModelForm):
    class Meta:
        model = CalificacionesPeriodoAcademico
        fields = '__all__'
    
    @transaction.atomic
    def save(self):
        #crear calificacion periodo academico
        calificacionesPerAca = CalificacionesPeriodoAcademico.objects.create()
        calificacionesPerAca.estudiante = Estudiantes.objects.get(id=self.cleaned_data.get('est_id'))
        calificacionesPerAca.clase = Clases.objects.get(id=self.cleaned_data.get("clas_id"))
        calificacionesPerAca.periodo_academido = PeriodoAcademico.objects.get(id=1)
        #calificaciones
        calificacionesPerAca.calificacion_1 = self.cleaned_data.get("cal_1")
        calificacionesPerAca.calificacion_2 = self.cleaned_data.get("cal_2")
        calificacionesPerAca.calificacion_3 = self.cleaned_data.get("cal_3")
        calificacionesPerAca.calificacion_4 = self.cleaned_data.get("cal_4")
        calificacionesPerAca.calificacion_5 = self.cleaned_data.get("cal_5")
        calificacionesPerAca.calificacion_6 = self.cleaned_data.get("cal_6")
        calificacionesPerAca.calificacion_7 = self.cleaned_data.get("cal_7")
        #heteroevaluacion
        calificacionesPerAca.heteroevaluacion = self.cleaned_data.get("het_eva")
        #examenBimestral
        calificacionesPerAca.examenBimestral = self.cleaned_data.get("exa_bim")
        #autoevaluacion
        calificacionesPerAca.examenBimestral = self.cleaned_data.get("aut_eva")
        #coevaluacion
        calificacionesPerAca.coevaluacion = self.cleaned_data.get("co_eva")
        #guarda calificacion
        calificacionesPerAca.save()

        #crear calificacion final periodo academico
        calificacionFinPerAca = CalificacionesFinalesPeriodosAcademicos.objects.create()
        calificacionFinPerAca.estudiante = Estudiantes.objects.get(
            id=self.cleaned_data.get('est_id')
        )
        calificacionFinPerAca.clase = Clases.objects.get(
            id=self.cleaned_data.get("clas_id")
        )
        calificacionFinPerAca.periodo_academido = PeriodoAcademico.objects.get(id=1)
        #obtenerCalificacionFinal()
        calificacionFinPerAca.calificacionFinal = self.obtenerCalificacionFinal(
            self.cleaned_data.get("het_eva"),
            self.cleaned_data.get("exa_bim"),
            self.cleaned_data.get("aut_eva"),
            self.cleaned_data.get("co_eva")
        )
        calificacionFinPerAca.nivelDesempeno = self.obtener_nivel_desempeno_calificacion(
            calificacionFinPerAca.calificacionFinal
        )
        calificacionFinPerAca.save()

        return calificacionesPerAca   


    def obtenerCalificacionFinal(self, het_eva, exa_bim, aut_eva, co_eva):
        #c??lculo de porcentajes de calificaciones
        het_eva = float( float(het_eva) * 0.7 )
        exa_bim = float( float(exa_bim) * 0.2 )
        aut_eva = float( float(aut_eva) * 0.05)
        co_eva  = float( float(co_eva) * 0.05)   
        #nota final
        cal_fin = float( het_eva + exa_bim + aut_eva + co_eva )
        print("calificacion final : " + cal_fin)
        return cal_fin

    def obtener_nivel_desempeno_calificacion(calificacion):
        nivel = 'SUPERIOR'
        if calificacion <= 2.9:
            nivel = 'BAJO'
        elif calificacion >= 3 and calificacion <= 3.9:
            nivel = 'BASICO'
        elif calificacion >= 4 and calificacion <= 4.5:
            nivel = 'ALTO'
        return nivel
