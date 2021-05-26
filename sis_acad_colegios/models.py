from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class Eps(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True)

class Departamentos(models.Model):
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return self.departamento

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.ciudad


class Tipos_documentos(models.Model):
    tipo_documento = models.CharField(max_length=200)


class Estratos_sociales(models.Model):
    estrato_social = models.CharField(max_length=200)


class Grupos_sanguineos(models.Model):
    grupo_sanguineo = models.CharField(max_length=200)


class Tipos_poblaciones(models.Model):
    tipo_poblacion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tipo_poblacion


class Niveles_academicos_docentes(models.Model):
    nivel_academico = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nivel_academico


class Sedes(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Estudiantes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    cod_estudiante = models.CharField(max_length=10, unique=True)
    dni = models.IntegerField(unique=True, null=False, default='1')
   # nombres = models.CharField(max_length=200, null=True)
   # apellidos = models.CharField(max_length=200, null=True)
    #direccion = models.CharField(max_length=200, null=True)
   # telefono  = models.IntegerField(null=True)
   # correo  = models.CharField(max_length=200, null=True)
    #fecha_nacimiento = models.DateField(null=True)
   # eps = models.ForeignKey(Eps, on_delete=models.DO_NOTHING, null=True)
   # departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING, null=True)
   # ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=True)
   # grupo_sanguineo = models.ForeignKey(Grupos_sanguineos, on_delete=models.DO_NOTHING, null=True)
  #  nivel_academico_docente no= models.ForeignKey(Niveles_academicos_docentes, on_delete=models.DO_NOTHING, null=True)
   # tipo_poblacion = models.ForeignKey(Tipos_poblaciones, on_delete=models.DO_NOTHING)

class Docentes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    dni = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.dni
    #nombres = models.CharField(max_length=200, null=True)
    #apellidos = models.CharField(max_length=200, null=True)
  #  telefono  = models.IntegerField(null=True)
   # correo  = models.CharField(max_length=200, null=True)
   # fecha_nacimiento = models.DateField(null=True)
   # eps = models.ForeignKey(Eps, on_delete=models.DO_NOTHING)
   # departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING)
   # ciudad = models.ForeignKey(Ciudades, on_delete=models.DO_NOTHING)
   # grupo_sanguineo = models.ForeignKey(Grupos_sanguineos, on_delete=models.DO_NOTHING)
   # nivel_academico_docente = models.ForeignKey(Niveles_academicos_docentes, on_delete=models.DO_NOTHING)


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



class Jornadas(models.Model):
    jornada = models.CharField(max_length=200)
    jornada_descripcion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.jornada
