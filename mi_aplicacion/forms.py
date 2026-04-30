from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

from mi_aplicacion.models import Escuela, Maestro
from django.contrib.auth.models import User, Group

class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('is_active', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '{{ texto_boton }}', css_class='btn btn-primary')
        )
        
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_active")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['username'])
        
        if commit:
            user.save()
            group = Group.objects.get(name='capturista')
            user.groups.add(group)
        return user




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