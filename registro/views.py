from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from registro.models import Participante
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


class ParticipanteCreate(CreateView):
	template_name_suffix = '_create_form'

	model = Participante
	fields = ['dni', 'email',  'nombre', 'apellido_paterno',
		'apellido_materno', 'sexo', 'fecha_nacimiento', 'departamento',
		'direccion', 'referencia', 'telefono_fijo', 'celular', 
		'profesion', 'empresa', 'cargo']


class ParticipanteUpdate(UpdateView):
	template_name_suffix = '_update_form'
	success_url = '/registro/detalle/'

	model = Participante
	fields = ['dni', 'email',  'nombre', 'apellido_paterno',
		'apellido_materno', 'sexo', 'fecha_nacimiento', 'departamento',
		'direccion', 'referencia', 'telefono_fijo', 'celular', 
		'profesion', 'empresa', 'cargo']

	def get_object(self):
		return get_object_or_404(Participante, pk=self.request.user.id)



class ParticipanteDetailView(DetailView):
	model = Participante

	def get_object(self):
		return get_object_or_404(Participante, pk=self.request.user.id)


def logout_view(request):
    logout(request)
    return redirect('login')