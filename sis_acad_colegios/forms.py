from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from .models import *

class AsignaturaForm(ModelForm):

    class Meta:
        model = Asignaturas
        fields = '__all__'

class SedeForm(ModelForm):
    class Meta:
        model = Sedes
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
