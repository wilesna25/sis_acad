from django.db import models
from django.contrib.auth.models import User
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


class Sedes(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


class Asignaturas(models.Model):
    asignatura = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.asignatura

class Niveles_academicos_docentes(models.Model):
    nivel_academico = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nivel_academico

class Jornadas(models.Model):
    jornada = models.CharField(max_length=200)
    jornada_descripcion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.jornada

class Personas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dni = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono  = models.IntegerField(null=True)
    correo  = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateField(null=True)
    eps = models.ForeignKey(Eps, on_delete=models.DO_NOTHING)
    departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.DO_NOTHING)
    grupo_sanguineo = models.ForeignKey(Grupos_sanguineos, on_delete=models.DO_NOTHING)

class Estudiantes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    acudiente = models.ForeignKey(Personas, to_field='dni', on_delete=models.DO_NOTHING)
    cod_estudiante = models.CharField(max_length=10, unique=True)

class Docentes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nivel_academico_docente = models.ForeignKey(Niveles_academicos_docentes, on_delete=models.DO_NOTHING)
