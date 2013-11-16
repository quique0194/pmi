from django.contrib import admin
from registro.models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('boleto', '__unicode__', 'dni')
	search_fields = ['boleto', 'dni', 'nombre', 'apellido_paterno', 'apellido_materno']

admin.site.register(Persona, PersonaAdmin)