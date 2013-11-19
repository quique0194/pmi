from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from registro.models import Participante
from registro.forms import ParticipanteCreateForm, ParticipanteUpdateForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


class ParticipanteCreate(FormView):
	template_name = 'registro/participante_create_form.html'
	success_url = '/registro/success_create'

	form_class = ParticipanteCreateForm


class SuccessCreateView(TemplateView):
	template_name = "registro/success_create.html"


class ParticipanteUpdate(UpdateView):
	template_name_suffix = '_update_form'
	success_url = '/registro/detalle/'
	form_class = ParticipanteUpdateForm

	def get_object(self):
		return get_object_or_404(Participante, pk=self.request.user.id)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ParticipanteUpdate, self).dispatch(*args, **kwargs)



class ParticipanteDetailView(DetailView):
	model = Participante

	def get_object(self):
		return get_object_or_404(Participante, pk=self.request.user.id)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ParticipanteDetailView, self).dispatch(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('login')