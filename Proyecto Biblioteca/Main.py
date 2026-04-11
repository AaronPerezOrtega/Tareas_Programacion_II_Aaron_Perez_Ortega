from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestor_prestamos import GestorPrestamos

libro1 = Libro("Peppa Pig","Bucanero","12345")
libro2 = Libro("Teoria de Evolucion del Ser Humano","Jorge el Curioso","12345")
usuario1 = Usuario("Aarón","2521583","Estudiante")

#gestor = GestorPrestamos()

#mensaje = gestor.realizar_prestamo(libro1,usuario1,"2026-03-07")

#print(mensaje)

#print(libro1.getDisponibilidad())

#gestor.listar_prestamos()

#print(libro1.getTitle())

#print(libro1 == libro2)

#print(usuario1)

print(usuario1)

print(usuario1.getTipoUsuario())
