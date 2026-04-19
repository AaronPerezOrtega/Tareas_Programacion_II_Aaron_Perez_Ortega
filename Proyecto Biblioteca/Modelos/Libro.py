class Libro:
    def __init__(self,Titulo,Autor,ISBN):
        self.__Titulo = Titulo
        self.__Autor = Autor
        self.__ISBN = ISBN
        self.__Disponibilidad = True 
    
    def getTitulo(self):
        return self.__Titulo
    
    def getAutor(self):
        return self.__Autor

    def getISBN(self):
        return self.__ISBN

    def getDisponibilidad(self):
        return self.__Disponibilidad
            
    def  prestar(self):
        if (self.__Disponibilidad):
            self.__Disponibilidad = False
            return True
        return False
    
    def devolver(self):
        self.__Disponibilidad = True

    def __str__(self):
        return f"{self.__Titulo}"
    
    def __repr__(self):
        return f"Libros('{self.__Titulo}', '{self.__Autor}')"
    
    def __eq__(self,other):
        return self.__Titulo == other.__Titulo