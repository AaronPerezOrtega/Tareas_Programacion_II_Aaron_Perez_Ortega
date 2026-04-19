class Prestamo:
    def __init__(self,libro,usuario,fechaprestamo):
        self.__Libro = libro
        self.__Usuario = usuario
        self.__FechaPrestamo = fechaprestamo

    def getUsuario(self):
        return self.__Usuario

    def getLibro(self):
        return self.__Libro

    def getFechaPrestamo(self):
        return self.__FechaPrestamo
        
    def __str__(self):
        return f"{self.__Usuario} -- {self.__Libro}"