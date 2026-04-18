from modelos.libro import Libro
from modelos.alumno import Alumno
from servicios.gestor_prestamos import GestorPrestamos


usuario1 = Alumno("Aarón","2521583")
libro1 = Libro("Tomie", "Junji Ito")
libro2 = Libro("Tomie II", "Junji Ito")
libro3 = Libro("Las Maldiciones Egoistas de Soichi", "Junji Ito")
libro4 = Libro("El Mortal Mal de Amores", "Junji Ito")
libro5 = Libro("El albergue del Desertor", "Junji Ito")
libro6 = Libro("El Callejon Trasero", "Junji Ito")
libro7 = Libro("Las Estatuas Sin Cabeza", "Junji Ito")
libro8 = Libro("El Desagüe Afligido", "Junji Ito")
libro9 = Libro("El Pueblo de Lapidas", "Junji Ito")

gestor = GestorPrestamos()

print("Disponible:", libro2.getDisponibilidad())

mensaje = gestor.realizar_prestamo(libro2, usuario1, "2026-04-18")

print(usuario1.descripcion())

print("Libro:", libro2)

print("Resultado:", mensaje)

print("Disponible:", libro2.getDisponibilidad())

gestor.listar_prestamos()

print()
