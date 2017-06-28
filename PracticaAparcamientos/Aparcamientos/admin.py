from django.contrib import admin
from Aparcamientos.models import Aparcamiento, ComentarioAparcamiento, Seleccionado, CSS

# Register your models here.

admin.site.register(Aparcamiento)
admin.site.register(ComentarioAparcamiento)
admin.site.register(Seleccionado)
admin.site.register(CSS)
