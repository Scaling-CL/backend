from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    rut = models.CharField(max_length=12, verbose_name="Rut")
    nombres = models.CharField(
        max_length=100, blank=True, verbose_name="Nombres")
    apellidos = models.CharField(
        max_length=100, blank=True, verbose_name="Apellidos")
    email = models.EmailField(
        max_length=100, blank=True, verbose_name="Correo electrónico")
    telefono = models.CharField(
        max_length=100, blank=True, verbose_name="Teléfono")
    celular = models.CharField(
        max_length=100, blank=True, verbose_name="Celular")
    direccion1 = models.CharField(
        max_length=100, blank=True, verbose_name="Dirección")
    direccion2 = models.CharField(
        max_length=100, blank=True, verbose_name="Dirección 2")
    comuna = models.CharField(
        max_length=100, blank=True, verbose_name="Comuna")
    ID_REGION = (('1', 'I Región de Tarapacá'),
                 ('2', 'II Región de Antofagasta'),
                 ('3', 'III Región de Atacama'),
                 ('4', 'IV Región de Coquimbo'),
                 ('5', 'V Región de Valparaíso'),
                 ('6', 'VI Región del Libertador General Bernardo O’Higgins'),
                 ('7', 'VII Región del Maule'),
                 ('8', 'VIII Región del Biobío'),
                 ('9', 'IX Región de La Araucanía'),
                 ('10', 'X Región de Los Lagos'),
                 ('11', 'XI Región Aysén del General Carlos Ibáñez del Campo'),
                 ('12', 'XII Región de Magallanes y Antártica Chilena'),
                 ('13', 'Región Metropolitana de Santiago'),
                 ('14', 'XIV Región de Los Ríos'),
                 ('15', 'XV Región de Arica y Parinacota'),
                 ('16', 'XVI Región de Ñuble'))
    region = models.CharField(
        max_length=100, choices=ID_REGION, blank=True, verbose_name="Región")
    pais = models.CharField(max_length=100, blank=True, verbose_name="País")
    TIPOS_FACTURACION = (('1', 'Boleta'), ('2', 'Factura'))
    tipoFacturacion = models.CharField(
        max_length=1, choices=TIPOS_FACTURACION, blank=True, verbose_name="Tipo de facturación")
    rutEmpresa = models.CharField(
        max_length=100, blank=True, verbose_name="Rut de la empresa")
    nombreEmpresa = models.CharField(
        max_length=100, blank=True, verbose_name="Nombre de la empresa")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


class Veterinaria(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    nombreVeterinario = models.CharField(
        max_length=100, blank=True, verbose_name="Nombre veterinario")
    email = models.EmailField(
        max_length=100, blank=True, verbose_name="Correo electrónico")
    telefono = models.CharField(
        max_length=100, blank=True, verbose_name="Teléfono")
    celular = models.CharField(
        max_length=100, blank=True, verbose_name="Celular")
    direccion1 = models.CharField(
        max_length=100, blank=True, verbose_name="Dirección")
    direccion2 = models.CharField(
        max_length=100, blank=True, verbose_name="Dirección 2")
    comuna = models.CharField(
        max_length=100, blank=True, verbose_name="Comuna")
    ID_REGION = (('1', 'I Región de Tarapacá'),
                 ('2', 'II Región de Antofagasta'),
                 ('3', 'III Región de Atacama'),
                 ('4', 'IV Región de Coquimbo'),
                 ('5', 'V Región de Valparaíso'),
                 ('6', 'VI Región del Libertador General Bernardo O’Higgins'),
                 ('7', 'VII Región del Maule'),
                 ('8', 'VIII Región del Biobío'),
                 ('9', 'IX Región de La Araucanía'),
                 ('10', 'X Región de Los Lagos'),
                 ('11', 'XI Región Aysén del General Carlos Ibáñez del Campo'),
                 ('12', 'XII Región de Magallanes y Antártica Chilena'),
                 ('13', 'Región Metropolitana de Santiago'),
                 ('14', 'XIV Región de Los Ríos'),
                 ('15', 'XV Región de Arica y Parinacota'),
                 ('16', 'XVI Región de Ñuble'))
    region = models.CharField(
        max_length=100, choices=ID_REGION, blank=True, verbose_name="Región")
    pais = models.CharField(max_length=100, blank=True, verbose_name="País")

    class Meta:
        verbose_name = "Veterinaria"
        verbose_name_plural = "Veterinarias"

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    veterinarioAnterior = models.ForeignKey(
        Veterinaria, null=True, on_delete=models.SET_NULL)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    TIPOS_SEXO = (('1', 'Macho'), ('2', 'Hembra'))
    sexo = models.CharField(max_length=1, choices=TIPOS_SEXO,
                            blank=True, verbose_name="Sexo")
    peso = models.IntegerField()

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nombre


class Alimentacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    fechaCreacion = models.DateField()
    tipoComida = models.CharField(max_length=100)
    marcaComida = models.CharField(max_length=100)
    pesoComida = models.IntegerField()
    nComidasDia = models.IntegerField()
    estado = models.BooleanField()


class Patologia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField()


class Ciclos_Celo(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()


class Muerte(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    idConsulta = models.IntegerField()
    razon = models.CharField(max_length=100)


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    fecha = models.IntegerField()
    idUsuario = models.IntegerField()
    razon = models.CharField(max_length=100)
    anamnesis = models.CharField(max_length=100)
    examenFisico = models.CharField(max_length=100)
    peso = models.IntegerField()
    temperatura = models.IntegerField()


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    exchange_id = models.CharField(max_length=255, null=True, blank=True)
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    event_subject = models.CharField(max_length=255, null=True, blank=True)
    event_location = models.CharField(max_length=255, null=True, blank=True)
    event_category = models.CharField(max_length=255, null=True, blank=True)
    event_attendees = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.event_id)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaCompra = models.DateField()
    fechaVencimiento = models.DateField()
    Descripción = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre