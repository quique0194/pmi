from django import forms
from django.forms import ModelForm, TextInput, RadioSelect
from registro.models import Participante

class ParticipanteCreateForm(ModelForm):
	class Meta:
		model = Participante
		exclude = ['user', 'boleto']
		widgets = {
			'dni': TextInput(attrs={'size': 50, 'title': 'Your name',}),
            'direccion': TextInput(attrs={'size': 50, 'title': 'Your name',}),
            'sexo': RadioSelect(choices=Participante.SEXOS),
            'status': RadioSelect,
        }

class ParticipanteUpdateForm(ModelForm):
	class Meta:
		model = Participante
		exclude = ['user', 'boleto', 'numero_operacion', 'monto', 'fecha_operacion']
		widgets = {
            'direccion': TextInput(attrs={'size': 50, 'title': 'Your name',}),
            'sexo': RadioSelect(choices=Participante.SEXOS),
            'status': RadioSelect,
        }