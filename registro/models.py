from django.db import models



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
	
	dni = models.PositiveIntegerField(unique=True)
	boleto = models.PositiveIntegerField(unique=True)
	email = models.EmailField(unique=True)

	nombre = models.CharField(max_length=45)
	apellido_paterno = models.CharField(max_length=45)
	apellido_materno = models.CharField(max_length=45)
	sexo = models.CharField(max_length=1, choices=SEXOS)
	fecha_nacimiento = models.DateField(help_text="Por favor utilice el siguiente formato: <em>DD/MM/AAAA</em>")
	departamento = models.PositiveIntegerField(choices=DEPARTAMENTOS, default=AREQUIPA, verbose_name="dpto")
	direccion = models.CharField(max_length=100)
	referencia = models.CharField(max_length=100, blank=True)
	telefono_fijo = models.CharField(max_length=9, blank=True)
	celular = models.CharField(max_length=12, blank=True)
	
	profesion = models.CharField(max_length=45, blank=True)
	empresa = models.CharField(max_length=45, blank=True)
	cargo = models.CharField(max_length=45, blank=True)


	def __unicode__(self):
		return self.nombre + ' ' + self.apellido_paterno +\
				 ' ' + self.apellido_materno

