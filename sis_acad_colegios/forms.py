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

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        print("a guardar")
        user = super().save(commit=False)
        user.first_name = self.cleaned_data('first_name')
        user.last_name = self.cleaned_data('last_name')
        user.save()
        print("creadooooo")
        docente = Docentes.objects.create(user=user)
        docente.dni = self.cleaned_data('dni')
        docente.direccion = self.cleaned_data('direccion')
        docente.save()
        return user
