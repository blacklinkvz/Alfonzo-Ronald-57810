from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"
    
    ordering = ["nombre"]
    
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
 
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.apellido},   {self.nombre}"
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ["nombre", "apellido"]

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.apellido},   {self.nombre}"

class Cita(models.Model):
    fecha = models.DateField()
    paciente = models.IntegerField()
    doctor = models.IntegerField()
    
class Ficha(models.Model):
    cita = models.IntegerField()
    diagnostico = models.TextField()
    receta = models.TextField()

    def __str__(self):
        return f"{self.cita},   {self.diagnostico}, {self.receta} "

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"