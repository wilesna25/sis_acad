from operator import mod
from statistics import mode
from tabnanny import verbose
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import date

from django.forms import ValidationError
from .manager import DocentesManager
# Create your models here.


class Jornadas(models.Model):
    jornada = models.CharField(max_length=200)
    jornada_descripcion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.jornada

    class Meta:
        verbose_name = "Jornada"
        verbose_name_plural = "Jornadas"


class Sedes(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"


class PeriodoAcademico(models.Model):
    periodo = models.CharField(max_length=200, null=True, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.periodo

    class Meta:
        verbose_name = "Periodo Académico"
        verbose_name_plural = "Periodos Académicos"


class AreasAsignaturas(models.Model):
    area = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "Área Asignatura"
        verbose_name_plural = "Áreas Asignaturas"


class Asignaturas(models.Model):
    asignatura = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    area = models.ForeignKey(AreasAsignaturas,  on_delete=models.CASCADE)

    def __str__(self):
        return self.asignatura

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"


class GradosAcademicos(models.Model):
    grado = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.grado

    class Meta:
        verbose_name = "Grado Académico"
        verbose_name_plural = "Grados Académicos"


class LogrosAsignaturas(models.Model):
    grado = models.ForeignKey(GradosAcademicos,  on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas,  on_delete=models.CASCADE)
    nivel_desempeno = models.CharField(max_length=50)
    logro = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = "Logro Asignatura"
        verbose_name_plural = "Logros Asignaturas"


class Docentes(AbstractUser):

    email = models.EmailField(unique=True)
    dni = models.IntegerField(unique=True, null=True)
    direccion = models.CharField(max_length=200, null=True)

    objects = DocentesManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.last_name + " " + self.first_name
        return self.email

    class Meta:
        db_table = "Docentes"
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"



class Grupos(models.Model):
    grupo = models.CharField(max_length=200, null=True)
    grado = models.ForeignKey(GradosAcademicos,  on_delete=models.CASCADE)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)

    def __str__(self):
        return self.grupo

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"


class Clases(models.Model):
    clase = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)

    def __str__(self):
        return self.clase

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

    
class Estudiantes(models.Model):
    cod_estudiante = models.CharField(max_length=10, unique=True)
    dni = models.IntegerField(unique=True, null=False, default='1')
    nombres = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.IntegerField(null=True)
    correo = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.apellidos + " " + self.nombres

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

class Matriculas(models.Model):
    estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, null=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(default=date.today)

    def __str__(self):
        return self.grupo.grupo + " - " + self.estudiante.cod_estudiante + " ; " + self.estudiante.apellidos + " " + self.estudiante.nombres
    
    class Matriculas:
        verbose_name = "Matriculas"
        verbose_name_plural = "Matriculas"


class Estudiantes_por_Grupo(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True)
    estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Estudiante por grupo"
    verbose_name_plural = "Estudiantes por grupos"

# creating a validator function
def validate_notas_conceptos_academicos(value):
    if value >0 and value <=5:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")
 

class ConceptosAcademicos(models.Model):
    grado_academico = models.ForeignKey(
        GradosAcademicos, on_delete=models.CASCADE, null=True)
    asignaturas = models.ForeignKey(
        Asignaturas, on_delete=models.CASCADE, null=True)
    periodo_academico = models.ForeignKey(
        PeriodoAcademico, on_delete=models.CASCADE, null=True)
    nota_maxima = models.FloatField(null=True, validators=[validate_notas_conceptos_academicos])
    nota_minima = models.FloatField(null=True, validators=[validate_notas_conceptos_academicos])
    concepto_academico = models.CharField(null=True, max_length=40000)
    
    class Meta:
        verbose_name = "Concepto Académico"
        verbose_name_plural = "Conceptos académicos"
    
    def __str__(self):
        return self.concepto_academico

class FallasAsistencias(models.Model):
    estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.DO_NOTHING, null=True)
    clase = models.ForeignKey(Clases, on_delete=models.DO_NOTHING, null=True)
    justificada = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=500, null=True)
    fecha = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Falla Asistencia"
        verbose_name_plural = "Falla Asistencias"


class Calificaciones(models.Model):
    estudiante = models.ForeignKey(
    Estudiantes, on_delete=models.DO_NOTHING, null=True)
    clase = models.ForeignKey(Clases, on_delete=models.DO_NOTHING, null=True)
    periodo_academico = models.IntegerField(null=True)
    calificacion = models.FloatField(null=True)
    nivel_desempeno = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return  self.clase.clase + " - " + self.estudiante.apellidos + " ===  " + str(self.calificacion);



class CalificacionesPeriodoAcademico(models.Model):
    
    estudiante = models.ForeignKey(
    Estudiantes, on_delete=models.CASCADE, null=True)

    clase = models.ForeignKey(Clases, on_delete=models.CASCADE, null=True)
    periodo_academico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE, null=True)

    #zona para las 7 calificaciones que agrega el docente
    calificacion_1 = models.FloatField(null=True)
    calificacion_2 = models.FloatField(null=True)
    calificacion_3 = models.FloatField(null=True)
    calificacion_4 = models.FloatField(null=True)
    calificacion_5 = models.FloatField(null=True)
    calificacion_6 = models.FloatField(null=True)
    calificacion_7 = models.FloatField(null=True)

    #heteroevaluación : nota calculada con el promedio de las 7 calificaciones anteriores
    heteroevaluacion = models.FloatField(null=True)
    #examen bimestral
    examenBimestral = models.FloatField(null=True)
    #autoevaluacion
    autoevaluacion = models.FloatField(null=True)
    #coevaluacion
    coevaluacion = models.FloatField(null=True)

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return  self.clase.clase + " - " + self.estudiante.apellidos ;



class CalificacionesFinalesPeriodosAcademicos(models.Model):

    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, null=True)
    clase = models.ForeignKey(Clases, on_delete=models.CASCADE, null=True)
    periodoAcademico = models.ForeignKey(PeriodoAcademico, on_delete=models.DO_NOTHING, null=True)
    calificacionFinal = models.FloatField(null=True)
    nivelDesempeno = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Calificacion final periodo académico."
        verbose_name_plural = "Calificaiones finales periodo académico"

    def __str__(self):
        if self.estudiante is not None:
            return str(self.calificacionFinal) + " " + self.estudiante.apellidos 


