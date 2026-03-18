from Modelos.Libro import Libro
from Modelos.Usuarios import Usuarios
from Servicios.Gestor_Prestamos import GestorPrestamos

libro1 = Libro("Peppa Pig","Bucanero","12345")
libro2 = Libro("Teoria de Evolucion del Ser Humano","Jorge el Curioso","12345")
usuario1 = Usuarios("Aarón","2521583")

gestor = GestorPrestamos()

mensaje = gestor.realizar_prestamo(libro1,usuario1,"2026-03-07")

#print(mensaje)

#print(libro1.getDisponibilidad())

#gestor.listar_prestamos()

#print(libro1.getTitle())

#print(libro1 == libro2)

print(usuario1)
