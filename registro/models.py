from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators  import RegexValidator
from django.core.validators  import MaxLengthValidator, MinLengthValidator
from django.core.validators  import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.core.mail import EmailMessage



def email_datos(participante):
	msj = "Este es un correo generado automaticamente. Por favor no responda a este mensaje.\n"
	msj = msj + "El objetivo de este mensaje es que usted pueda revisar su informacion para el congreso de PMI 2013.\n\n"
	msj = msj + "BOLETO: " + str(participante.boleto) + "\n"

	msj = msj + "\nINFORMACION PERSONAL:\n"
	msj = msj + "DNI: " + str(participante.dni) + "\n"
	msj = msj + "Nombre completo: " + participante.nombre  + " " + participante.apellido_paterno + \
		participante.apellido_materno + "\n"
	msj = msj + "Sexo: " + participante.get_sexo_display() + "\n"
	if participante.fecha_nacimiento:
		msj = msj + "Fecha de nacimiento: " + str(participante.fecha_nacimiento) + "\n"
	msj = msj + "Departamnto: " + participante.get_departamento_display() + "\n"
	if participante.direccion:
		msj = msj + "Direccion: " + participante.direccion + "\n"
	if participante.referencia:
		msj = msj + "Referencia: " + participante.referencia + "\n"
	if participante.telefono_fijo:
		msj = msj + "Telefono fijo: " + participante.telefono_fijo + "\n"
	if participante.celular:
		msj = msj + "Celular: " + participante.celular + "\n"
	msj = msj + "\nSTATUS:\n"
	msj = msj + "Status: " + participante.get_status_display() + "\n"
	if participante.status == participante.ESTUDIANTE:
		msj = msj + "Carnet universitario: " + participante.carnet_universitario + "\n"
	if participante.status == participante.PROFESIONAL:
		msj = msj + "Profesion: " + participante.profesion + "\n"
		msj = msj + "Empresa: " + participante.empresa + "\n"
		msj = msj + "Cargo: " + participante.cargo + "\n"
	msj = msj + "\nPMI:\n"
	msj = msj + "Miembro PMI: " + str(participante.miembro_pmi) + "\n"
	if participante.miembro_pmi:
		msj = msj + "Numero miembro PMI: " + participante.numero_miembro_pmi + "\n"
	msj = msj + "\nBOUCHER:\n"
	if participante.numero_operacion:
		msj = msj + "Numero de operacion: " + str(participante.numero_operacion) + "\n"
		msj = msj + "Monto: " + str(participante.monto) + "\n"
		msj = msj + "Fecha de operacion: " + str(participante.fecha_operacion) + "\n"
	msj = msj + "\nFACTURA:\n"
	msj = msj + "Factura: " + str(participante.factura) + "\n"
	if participante.factura:
		msj = msj + "Ruc: " + participante.ruc + "\n"
		msj = msj + "Nombre juridico: " + participante.nombre_juridico + "\n"
		msj = msj + "Direccion fiscal: " + participante.direccion_fiscal + "\n"
	msj = msj + "\n Si desea cambiar algo, puedo hacerlo con toda confianza en nuestra pagina web:\n"
	msj = msj + """http://199.175.48.205:8000/registro/modificar/"""

	email = EmailMessage('Datos PMI 2013', msj, to=[participante.email])
	email.send()



class Participante(models.Model):
	MASCULINO = 'M'
	FEMENINO = 'F'
	SEXOS = (
		(MASCULINO, 'Masculino'),
		(FEMENINO, 'Femenino'),	
	)

	AMAZONAS = 0
	ANCASH = 1
	APURIMAC = 2 
	AREQUIPA = 3
	AYACUCHO = 4
	CAJAMARCA = 5
	CALLAO = 6
	CUSCO = 7
	HUANCAVELICA = 8
	HUANUCO = 9
	ICA = 10
	JUNIN = 11
	LA_LIBERTAD = 12
	LAMBAYEQUE = 13
	LIMA = 14
	LORETO = 15
	MADRE_DE_DIOS = 16
	MOQUEGUA = 17
	PASCO = 18
	PIURA = 19
	PUNO = 20
	SAN_MARTIN = 21
	TACNA = 22
	TUMBES = 23
	UCAYALI = 24
	DEPARTAMENTOS = (
	    (AMAZONAS, 'Amazonas'),
		(ANCASH, 'Ancash'),
		(APURIMAC, 'Apurimac'),
		(AREQUIPA, 'Arequipa'),
		(AYACUCHO, 'Ayacucho'),
		(CAJAMARCA, 'Cajamarca'),
		(CALLAO, 'Callao'),
		(CUSCO, 'Cusco'),
		(HUANCAVELICA, 'Huancavelica'),
		(HUANUCO, 'Huanuco'),
		(ICA, 'Ica'),
		(JUNIN, 'Junin'),
		(LA_LIBERTAD, 'La Libertad'),
		(LAMBAYEQUE, 'Lambayeque'),
		(LIMA, 'Lima'),
		(LORETO, 'Loreto'),
		(MADRE_DE_DIOS, 'Madre de Dios'),
		(MOQUEGUA, 'Moquegua'),
		(PASCO, 'Pasco'),
		(PIURA, 'Piura'),
		(PUNO, 'Puno'),
		(SAN_MARTIN, 'San Martin'),
		(TACNA, 'Tacna'),
		(TUMBES, 'Tumbes'),
		(UCAYALI, 'Ucayali'),
	)

	ESTUDIANTE = 0
	PROFESIONAL = 1
	MIEMBRO_PMI = 2
	NO_MIEMBRO = 3

	STATUS = (
		(ESTUDIANTE, 'Estudiante'),
		(PROFESIONAL, 'Profesional'),
	)



	user = models.OneToOneField(User, primary_key=True)
	
	# requeridos

	dni = models.CharField(max_length=8, unique=True, db_index=True, 
		validators = [RegexValidator(r"^[0-9]*$",'Solo se puede ingresar digitos'), MaxLengthValidator(8), MinLengthValidator(8)])
	boleto = models.PositiveIntegerField(unique=True, db_index=True, 
		validators = [MaxValueValidator(999)])
	email = models.EmailField(unique=True)

	# datos personales

	nombre = models.CharField(max_length=45)
	apellido_paterno = models.CharField(max_length=45)
	apellido_materno = models.CharField(max_length=45)
	sexo = models.CharField(max_length=1, default=MASCULINO,choices=SEXOS)
	fecha_nacimiento = models.DateField(blank=True, null=True, help_text="<em>DD/MM/AAAA</em>")
	departamento = models.PositiveIntegerField(choices=DEPARTAMENTOS, default=AREQUIPA, verbose_name="dpto")
	direccion = models.CharField(max_length=100, blank=True)
	referencia = models.CharField(max_length=100, blank=True)
	telefono_fijo = models.CharField(max_length=9, blank=True, 
		validators = [RegexValidator(r"^[0-9]*$",'Solo se puede ingresar digitos')])
	celular = models.CharField(max_length=12, blank=True, 
		validators = [RegexValidator(r"^[0-9]*$",'Solo se puede ingresar digitos')])
	
	# informacion laboral

	status = models.PositiveIntegerField(choices=STATUS, default=PROFESIONAL)
	carnet_universitario = models.CharField(max_length=15, blank=True, help_text='Solo estudiantes', 
		validators = [RegexValidator(r"^([0-9]|-)*$",'Solo se puede ingresar digitos y guiones')])
	profesion = models.CharField(max_length=45, blank=True, help_text='Solo profesionales')
	empresa = models.CharField(max_length=45, blank=True, help_text='Solo profesionales')
	cargo = models.CharField(max_length=45, blank=True, help_text='Solo profesionales')

	# pmi

	miembro_pmi = models.BooleanField()
	numero_miembro_pmi = models.CharField(max_length=45, blank=True, help_text='Solo miembros pmi', 
		validators = [RegexValidator(r"^([0-9]|-)*$",'Solo se puede ingresar digitos y guiones')])

	# Boucher

	numero_operacion = models.PositiveIntegerField( blank=True, null=True, help_text =\
		""" Ejemplo: <a href="http://www.construccion.org/nosotros/verboucherBCP.htm" target="_blank">Boucher BCP</a>""")
	monto = models.PositiveIntegerField(blank=True, null=True)
	fecha_operacion = models.DateField(blank=True, null=True, help_text="<em>DD/MM/AAAA</em>")

	# Factura

	factura = models.BooleanField()
	ruc = models.CharField(max_length=11, blank=True, help_text="Solo si desea factura",
		validators = [RegexValidator(r"^[0-9]*$",'Solo se puede ingresar digitos'), MaxLengthValidator(11), MinLengthValidator(11)])
	nombre_juridico = models.CharField(max_length=45, blank=True, help_text="Solo si desea factura")
	direccion_fiscal = models.CharField(max_length=100, blank=True, help_text="Solo si desea factura")



	def __unicode__(self):
		return self.nombre + ' ' + self.apellido_paterno +\
				 ' ' + self.apellido_materno

	def save(self, *args, **kwargs):
		if not self.boleto:
			max_boleto = Participante.objects.filter(boleto__range=(500,599)).aggregate(Max('boleto'))['boleto__max']
			if max_boleto:
				self.boleto = max_boleto+1
			else:
				self.boleto = 500
		# modification
		try:
			self.user.username = self.dni
			self.user.set_password(self.boleto)
			self.user.save()
		# creation
		except:
			user = User.objects.create_user(username=self.dni, password=self.boleto)
			self.user = user
		
		email_datos(self)
		super(Participante, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('registro:detalle', kwargs={'pk': self.pk})



@receiver(post_delete, sender=Participante)
def participante_delete(sender, instance, **kwargs):
	instance.user.delete()