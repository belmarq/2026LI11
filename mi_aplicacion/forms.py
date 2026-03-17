from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

from mi_aplicacion.models import Escuela, Maestro

class EscuelaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar'))

    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]

class MaestroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaestroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre'), css_class='form-group col-md-4 mb-0'),
                Column(Field('sexo'), css_class='form-group col-md-4 mb-0'),
                Column(Field('fecha_nacimiento'), css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(Field('escuela'), css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '{{ texto_submit }}')
        )

    class Meta:
        model = Maestro
        fields = ["nombre", "escuela", "sexo", "fecha_nacimiento"]
        labels = {
            'nombre': 'Nombre del Maestro', 
            'escuela': 'Escuela a la que pertenece',
            'sexo': 'Sexo del Maestro',
            'fecha_nacimiento': 'Fecha de Nacimiento del Maestro'
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }