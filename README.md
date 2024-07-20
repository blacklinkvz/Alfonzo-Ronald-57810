Nombre del proyecto: Consultorio
Objetivo del proyecto: Registrar información basica referente a un consultorio medico, en el mismo se debe registrar las especialidades, doctores con email de contacto, creción de citas medicas, y fichas de la citas agendadas donde se guarde el diagnostico y la receta.

Modelos:

Especialidad:
nombre - varchar(100)

Doctor:
nombre - varchar(100)
apellido - varchar(100)
email - varchar(100)

Paciente:
nombre - varchar(100)
apellido - varchar(100)
email - varchar(100)

Cita:
fecha - date
paciente - int(fk)
doctor - int(fk)

Ficha:
cita - int(fk)
diagnostico - text
receta - text

Usuario administrador: admin
Contraseña: Coder12345*
