from django.contrib import admin
from registro.models import Participante

# Register your models here.


class ParticipanteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['dni','boleto','email']}),
        ('Informacion personal', {'fields': ['nombre','apellido_paterno',
            'apellido_materno','sexo','fecha_nacimiento','departamento','direccion',
            'referencia', 'telefono_fijo', 'celular']}),
        ('Informacion laboral',{'fields':['status', 'carnet_universitario','profesion', 'empresa',
            'cargo', 'numero_miembro_pmi']}),
        ('Voucher',{'fields': ['numero_operacion', 'monto', 'fecha_operacion']}),
    ]
    radio_fields = {'sexo': admin.HORIZONTAL , 'status': admin.VERTICAL}
    list_display = ('boleto', '__unicode__', 'dni')
    search_fields = ['boleto', 'dni', 'nombre', 'apellido_paterno', 'apellido_materno']
    

admin.site.register(Participante, ParticipanteAdmin)