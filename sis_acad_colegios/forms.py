from django.forms import ModelForm
from .models import Asignaturas, Sedes

class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'

class SedeForm(ModelForm):
    class Meta:
        model = Sedes
        fields = '__all__'