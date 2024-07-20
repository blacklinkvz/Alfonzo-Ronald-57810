from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import UserEditForm


# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def citas(request):
    contexto = {"citas": Cita.objects.all()}
    return render(request, "entidades/citas.html")

#__Especialidad__#

@login_required
def especialidades(request):
    contexto = {"especialidades": Especialidad.objects.all()}
    return render(request, "entidades/especialidades.html", contexto)

@login_required
def especialidadForm(request):
    if request.method == "POST":
        miForm = EspecialidadForm(request.POST)
        if miForm.is_valid():
            especialidad_nombre = miForm.cleaned_data.get("nombre")
            especialidad = Especialidad(nombre=especialidad_nombre)
            especialidad.save()
            contexto = {"especialidades": Especialidad.objects.all()}
            return render(request, "entidades/especialidades.html", contexto)
    else:
        miForm = EspecialidadForm()
        return render(request, "entidades/especialidadForm.html", {"form": miForm})

@login_required    
def buscarEspecialidad(request):
    return render(request, "entidades/buscarEspecialidad.html")

@login_required
def encontrarEspecialidad(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        especialidades = Especialidad.objects.filter(nombre__icontains=patron)
        contexto = {'especialidades': especialidades}
    else:
        contexto = {'especialidades': Especialidad.objects.all()}
        
    return render(request, "entidades/especialidades.html", contexto)

@login_required
def especialidadUpdate(request,id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    if request.method == "POST":
        miForm = EspecialidadForm(request.POST)
        if miForm.is_valid():
            especialidad.nombre = miForm.cleaned_data.get("nombre")
            especialidad.save()
            contexto = {"especialidades": Especialidad.objects.all()}
            return render(request, "entidades/especialidades.html", contexto)
    else:
        miForm = EspecialidadForm(initial={"nombre": especialidad.nombre,})
        return render(request, "entidades/especialidadForm.html", {"form": miForm})

@login_required    
def especialidadDelete(request,id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    especialidad.delete()
    contexto = {"especialidades": Especialidad.objects.all()}
    return render(request, "entidades/especialidades.html", contexto)

#__Doctor__#
@login_required
def doctores(request):
    contexto = {"doctores": Doctor.objects.all()}
    return render(request, "entidades/doctores.html", contexto)

@login_required
def doctorForm(request):
    if request.method == "POST":
        miForm = DoctorForm(request.POST)
        if miForm.is_valid():
            doctor_nombre = miForm.cleaned_data.get("nombre")
            doctor_apellido = miForm.cleaned_data.get("apellido")
            doctor_email = miForm.cleaned_data.get("email")
            doctor = Doctor(nombre=doctor_nombre,apellido=doctor_apellido,email=doctor_email)
            doctor.save()
            contexto = {"doctores": Doctor.objects.all()}
            return render(request, "entidades/doctores.html", contexto)
    else:
        miForm = DoctorForm()
        return render(request, "entidades/doctorForm.html", {"form": miForm}) 
    
@login_required
def buscarDoctor(request):
    return render(request, "entidades/buscarDoctor.html")

@login_required
def encontrarDoctor(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        doctores = Doctor.objects.filter(nombre__icontains=patron)
        contexto = {'doctores': doctores}
    else:
        contexto = {'doctores': Doctor.objects.all()}
        
    return render(request, "entidades/doctores.html", contexto)

@login_required
def doctorUpdate(request,id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    if request.method == "POST":
        miForm = DoctorForm(request.POST)
        if miForm.is_valid():
            doctor.nombre = miForm.cleaned_data.get("nombre")
            doctor.apellido = miForm.cleaned_data.get("apellido")
            doctor.email = miForm.cleaned_data.get("email")
            doctor.save()
            contexto = {"doctores": Doctor.objects.all()}
            return render(request, "entidades/doctores.html", contexto)
    else:
        miForm = DoctorForm(initial={"nombre": doctor.nombre, "apellido": doctor.apellido, "email": doctor.email})
        return render(request, "entidades/doctorForm.html", {"form": miForm})

@login_required    
def doctorDelete(request,id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    doctor.delete()
    contexto = {"doctores": Doctor.objects.all()}
    return render(request, "entidades/doctores.html", contexto)

#__ficha__#

class FichaList(ListView,LoginRequiredMixin):
    model = Ficha

class FichaCreate(CreateView,LoginRequiredMixin):
    model = Ficha
    fields = ["cita","diagnostico","receta"]
    success_url = reverse_lazy("ficha")

class FichaUpdate(UpdateView,LoginRequiredMixin):
    model = Ficha
    fields = ["cita","diagnostico","receta"]
    success_url = reverse_lazy("ficha")

class FichaDelete(DeleteView,LoginRequiredMixin):
    model = Ficha
    success_url = reverse_lazy("ficha")

#__Cita__#

class CitaList(ListView,LoginRequiredMixin):
    model = Cita

class CitaCreate(CreateView,LoginRequiredMixin):
    model = Cita
    fields = ["fecha","paciente","doctor"]
    success_url = reverse_lazy("cita")

class CitaUpdate(UpdateView,LoginRequiredMixin):
    model = Cita
    fields = ["cita","diagnostico","receta"]
    success_url = reverse_lazy("cita")

class CitaDelete(DeleteView,LoginRequiredMixin):
    model = Cita
    success_url = reverse_lazy("cita")

#__Login Logout register__#

def loginRequest(request):
    if request.method == ("POST"):
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == ("POST"):
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})

#___Edicion de perfil y avatar__#

@login_required
def editProfile(request):
    user = request.user

    if request.method == "POST":
        miForm = UserEditForm(request.POST, instance=user)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=user)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class cambiarClave(LoginRequiredMixin,PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #borrar avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #enviar imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})

def acercaDe(request):
    return render(request, "entidades/acercaDe.html")