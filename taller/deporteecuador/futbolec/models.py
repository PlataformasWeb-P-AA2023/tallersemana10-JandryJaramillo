from django.db import models

class Equipo(models.Model):
    
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s - %s - %s" % (self.nombre,
                                 self.siglas,
                                 self.user)

class Jugador(models.Model):

    opciones_posicion_jugador = (
        ('centro', 'Central'),
        ('arquero', 'Arquero'),
        ('delantero', 'Delantero'),
        ('defensa', 'Defensa'),
        )

    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30, \
            choices=opciones_posicion_jugador)
    nroCamiseta = models.IntegerField("Número de camiseta", unique=True)
    sueldo = models.IntegerField("Sueldo")  

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


    def __str__(self):
        return "%s - %s - %d - %d" % (self.nombre,
                self.posicion,
                self.nroCamiseta,
                self.sueldo)

class Campeonato(models.Model):
    
    nombre_de_campeonato = models.CharField(max_length=30)
    nombre_de_auspiciante = models.CharField(max_length=30)    
  
    def __str__(self):
        return "%s - %s" % (self.nombre_de_campeonato,
                            self.nombre_de_auspiciante)


class CampeonatoEquipos(models.Model):
    
    año = models.IntegerField("Año")
    
    equipo_de_futbol = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Campeonato Equipos: Año: %d - Equipo(%s) - Campeonato(%s)" % \
                (self.año, self.equipo_de_futbol, self.campeonato)
