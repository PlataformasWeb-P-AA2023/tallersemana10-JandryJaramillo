from django.db import models

class Jugador(models.Model):

    opciones_posicion_jugador = (
        ('centro', 'Central'),
        ('arquero', 'Arquero'),
        ('delantero', 'Delantero'),
        ('defensa', 'Defensa'),
        )

    nombre = models.CharField(max_length=30)
    posicion_campo = models.CharField(max_length=30, \
            choices=opciones_posicion_jugador)
    nro_camiseta = models.IntegerField("Número de camiseta", unique=True)
    sueldo = models.IntegerField("Sueldo")  

    equipo_de_futbol = models.ManyToManyField('Modulo', through='Matricula')


    def __str__(self):
        return "%s - %s - %s - edad: %d - tipo: %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.edad,
                self.tipo_estudiante)


class Modulo(models.Model):
    """
    """
    opciones_modulo = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        )

    nombre = models.CharField(max_length=30, \
            choices=opciones_modulo)
    estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

    def __str__(self):
        return "Módulo: %s" % (self.nombre)


class CampeonatoEquipos(models.Model):
    """
    """
    estudiante = models.ForeignKey(Estudiante, related_name='lasmatriculas',
            on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, related_name='lasmatriculas',
            on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return "Matricula: Estudiante(%s) - Modulo(%s)" % \
                (self.estudiante, self.modulo.nombre)
