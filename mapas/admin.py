from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dependencia, Subcategoria, PuntoMapa

# En lugar de admin.site.register, usamos decoradores y la nueva librería

@admin.register(Dependencia)
class DependenciaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Subcategoria)
class SubcategoriaAdmin(ImportExportModelAdmin):
    pass

@admin.register(PuntoMapa)
class PuntoMapaAdmin(ImportExportModelAdmin):
    pass