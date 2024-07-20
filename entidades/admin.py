from django.contrib import admin

# Register your models here.
from .models import *

class DoctorAdmin (admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email")

class FichaAdmin (admin.ModelAdmin):
    list_display = ("cita", "diagnostico", "receta")

admin.site.register(Especialidad)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Cita)
admin.site.register(Ficha, FichaAdmin)