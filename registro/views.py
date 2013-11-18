from django.views.generic.edit import CreateView, UpdateView
from registro.models import Participante



class ParticipanteCreate(CreateView):
	template_name_suffix = '_create_form'

	model = Participante
	fields = ['dni', 'email',  'nombre', 'apellido_paterno',
		'apellido_materno', 'sexo', 'fecha_nacimiento', 'departamento',
		'direccion', 'referencia', 'telefono_fijo', 'celular', 
		'profesion', 'empresa', 'cargo']


class ParticipanteUpdate(UpdateView):
	template_name_suffix = '_update_form'

	model = Participante
	fields = ['dni', 'email',  'nombre', 'apellido_paterno',
		'apellido_materno', 'sexo', 'fecha_nacimiento', 'departamento',
		'direccion', 'referencia', 'telefono_fijo', 'celular', 
		'profesion', 'empresa', 'cargo']