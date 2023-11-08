from django.contrib import admin
from .models import Cliente, Medico, Cita

admin.site.register(Cliente)
admin.site.register(Medico)
admin.site.register(Cita)