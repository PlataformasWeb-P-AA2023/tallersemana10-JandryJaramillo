from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Jugador, Equipo, Campeonato, CampeonatoEquipos
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):   
    list_display = ('nombre', 'posicion', 'nroCamiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'posicion', 'equipo')

admin.site.register(Jugador, JugadorAdmin)

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):   
    list_display = ('nombre', 'siglas', 'user')
    search_fields = ('nombre', 'siglas', 'user')

admin.site.register(Equipo, EquipoAdmin)

class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):   
    list_display = ('nombre_de_campeonato', 'nombre_de_auspiciante')
    search_fields = ('nombre_de_campeonato', 'nombre_de_auspiciante')

admin.site.register(Campeonato, CampeonatoAdmin)

admin.site.register(CampeonatoEquipos)