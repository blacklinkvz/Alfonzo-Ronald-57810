from django.urls import path, include
from entidades.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    
    path('citas/', citas, name="citas"),
    #path('fichas/', citas, name="fichas"),
    
    #__especialidades__#
    path('especialidades/', especialidades, name="especialidades"),
    path('especialidadForm/', especialidadForm, name="especialidadForm"),
    path('buscarEspecialidad/', buscarEspecialidad, name="buscarEspecialidad"),
    path('encontrarEspecialidad/', encontrarEspecialidad, name="encontrarEspecialidad"),
    path('especialidadUpdate/<id_especialidad>/', especialidadUpdate, name="especialidadUpdate"),
    path('especialidadDelete/<id_especialidad>/', especialidadDelete, name="especialidadDelete"),
    
    #__doctores__#
    path('doctores/', doctores, name="doctores"),
    path('doctorForm/', doctorForm, name="doctorForm"),
    path('buscarDoctor/', buscarDoctor, name="buscarDoctor"),
    path('encontrarDoctor/', encontrarDoctor, name="encontrarDoctor"),
    path('doctorUpdate/<id_doctor>/', doctorUpdate, name="doctorUpdate"),
    path('doctorDelete/<id_doctor>/', doctorDelete, name="doctorDelete"),

    #__Fichas__#
    path('ficha/', FichaList.as_view(), name="ficha"),
    path('fichaCreate/', FichaCreate.as_view(), name="fichaCreate"),
    path('fichaUpdate/<int:pk>', FichaUpdate.as_view(), name="fichaUpdate"),
    path('fichaDelete/<int:pk>', FichaDelete.as_view(), name="fichaDelete"),

    #__Citas__#
    path('cita/', CitaList.as_view(), name="cita"),
    path('citaCreate/', CitaCreate.as_view(), name="citaCreate"),
    path('citaUpdate/<int:pk>', CitaUpdate.as_view(), name="citaUpdate"),
    path('citaDelete/<int:pk>', CitaDelete.as_view(), name="citaDelete"),

    #__Login Logout register__#
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #__Edicion perfil y avatar__#
     path('perfil/', editProfile, name="perfil"),
     path('<int:pk>/password/', cambiarClave.as_view(), name="cambiarClave"),
     path('agregar_avatar/', agregarAvatar, name='agregarAvatar'),

    #__AcercaDe__#
    path('acercaDe/', acercaDe, name="acercaDe"),

]
