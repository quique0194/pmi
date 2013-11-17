from django.views.generic.edit import CreateView, UpdateView
from registro.models import Participante



class ParticipanteCreate(CreateView):
	template_name_suffix = '_create_form'

	model = Participante
	fields = ['nombre', 'apellido_paterno','apellido_materno']


class ParticipanteUpdate(UpdateView):
	template_name_suffix = '_update_form'

	model = Participante
	fields = ['nombre', 'apellido_paterno','apellido_materno']