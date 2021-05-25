from django.forms import ModelForm
from .models import Asignaturas, Sedes, AreasAsignaturas

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