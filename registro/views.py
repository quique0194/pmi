from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from registro.models import Participante
from registro.forms import ParticipanteCreateForm, ParticipanteUpdateForm
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect



class ParticipanteCreate(FormView):
	template_name = 'registro/participante_create_form.html'
	success_url = '/registro/success_create'

	form_class = ParticipanteCreateForm

	def form_valid(self, form):
		form.save()
		self.request.session['boleto'] = form.instance.boleto
		return super(ParticipanteCreate, self).form_valid(form)



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
    return redirect('registro:login')


@csrf_protect
def login_view(request):
	logout(request)
	msj = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('registro:detalle')
		else:
			msj = 'Dni o boleto incorrectos'

	return render_to_response('registro/login.html', { 'msj': msj }, context_instance=RequestContext(request))



class SuccessCreateView(TemplateView):
	template_name = "registro/success_create.html"

def  success_create_view(request):
	return render_to_response('registro/success_create.html', {'boleto': request.session['boleto']},\
		context_instance=RequestContext(request))