class Prestamo:
    def __init__(self,Libro,Usuario,FechaPrestamo):
        self.__Usuario = Usuario
        self.__Libro = Libro
        self.__FechaPrestamo = FechaPrestamo

    def getUsuario(self):
        return self.__Usuario

    def getLibro(self):
        return self.__Libro

    def getFechaPrestamo(self):
        return self.__FechaPrestamo
        
    def __str__(self):
        return f"{self.__Usuario} -- {self.__Libro}"