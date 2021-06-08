from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import date
# Create your models here.


class Jornadas(models.Model):
    jornada = models.CharField(max_length=200)
    jornada_descripcion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.jornada


class Sedes(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class PeriodoAcademico(models.Model):
    periodo = models.CharField(max_length=200, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.periodo


class Departamentos(models.Model):
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return self.departamento

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.ciudad


#class Niveles_academicos_docentes(models.Model):
  #  nivel_academico = models.CharField(max_length=200, null=True)
#
   # def __str__(self):
   #     return self.nivel_academico


class AreasAsignaturas(models.Model):
    area = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.area


class Asignaturas(models.Model):
    asignatura = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    area = models.ForeignKey(AreasAsignaturas,  on_delete=models.CASCADE)

    def __str__(self):
        return self.asignatura


class GradosAcademicos(models.Model):
    grado = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.grado

class LogrosAsignaturas(models.Model):
    grado =  models.ForeignKey(GradosAcademicos,  on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas,  on_delete=models.CASCADE)
    nivel_desempeno = models.CharField(max_length=50)
    logro = models.CharField(max_length=500)


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Docentes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    dni = models.IntegerField(unique=True, null=True)
    direccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.first_name
    #nombres = models.CharField(max_length=200, null=True)
    #apellidos = models.CharField(max_length=200, null=True)
  #  telefono  = models.IntegerField(null=True)
   # correo  = models.CharField(max_length=200, null=True)
   # fecha_nacimiento = models.DateField(null=True)
   # departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING)
   # ciudad = models.ForeignKey(Ciudades, on_delete=models.DO_NOTHING)
   # nivel_academico_docente = models.ForeignKey(Niveles_academicos_docentes, on_delete=models.DO_NOTHING)


class Grupos(models.Model):
    grupo = models.CharField(max_length=200,null=True)
    grado = models.ForeignKey(GradosAcademicos,  on_delete=models.CASCADE)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)

    def __str__(self):
        return self.grupo

#asignacion academica
class Clases(models.Model):
    clase = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)

    def __str__(self):
        return self.clase


class Estudiantes(models.Model):
    cod_estudiante = models.CharField(max_length=10, unique=True)
    dni = models.IntegerField(unique=True, null=False, default='1')
    nombres = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono  = models.IntegerField(null=True)
    correo  = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateField(null=True)
   # nombres_acudiente = models.CharField(max_length=200, null=True)
   # telefonos_acudiente = models.IntegerField()
    #direccion_acudiente = models.CharField(max_length=200, null=True)
    #eps = models.ForeignKey(Eps, on_delete=models.DO_NOTHING, null=True)
   # departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING, null=True)
    #ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=True)


class Matriculas(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.DO_NOTHING, null=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.DO_NOTHING, null=True)
    fecha = models.DateField(default=date.today)


class Estudiantes_por_Grupo(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.DO_NOTHING, null=True)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.DO_NOTHING, null=True)


class FallasAsistencias(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.DO_NOTHING, null=True)
    clase = models.ForeignKey(Clases, on_delete=models.DO_NOTHING, null=True)
    justificada = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=500, null=True)
    fecha = models.DateField(default=date.today)

class Calificaciones(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.DO_NOTHING, null=True)
    clase = models.ForeignKey(Clases, on_delete=models.DO_NOTHING, null=True)
    periodo_academico = models.IntegerField(null=True)
    calificacion = models.FloatField(null=True)
    nivel_desempeno = models.CharField(max_length=50, null=True)