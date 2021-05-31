from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from .models import *


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
        #crea matrícula
        matricula = Matriculas.objects.create(estudiante=estudiante)
        matricula.grupo = Grupos.objects.get(id=self.cleaned_data.get('grupo'))
        matricula.save()
        #crear Estudiante_por_Grupo
        est_x_grupo = Estudiantes_por_Grupo.objects.create(estudiante=estudiante, grupo=matricula.grupo)
        est_x_grupo.save()
        return estudiante
