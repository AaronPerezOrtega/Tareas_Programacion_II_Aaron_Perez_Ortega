#Tiempo Constante: (O(1))
#Un numero perfecto es aquel que la suma de sus divisores es igual al numero
def numerosperfectos(arr):
    print(f"Complejidad O(1):Tiempo Constante")
    arr = [6,28,496,8128]
    return arr

#Tiempo Logaritmo: (O(logn))
def rondastorneo(arr):
    print(f"Complejidad O(logn):Tiempo logaritmico")
    jugadores = int(input("Cuantos jugadores van a ser\n"))
    ronda = 0
    while jugadores > 1:
        ronda += 1
        jugadores = jugadores // 2
        arr.append(f"Ronda {ronda}, son {jugadores} jugadores")
    return arr
        
#Tiempo lineal: (O(n))
def multiplosde9(arr):
    print(f"Complejidad O(n):Tiempo Lineal")
    n = int(input(f"Hasta que numero se van a analizar los multiplos de 9\n"))
    for i in range(1,n+1,1):
            if i % 9 == 0:
                    arr.append(i)
    return arr

#Tiempo Lineal: (O(nlogn))
def niveldexpmenoramayor(arr):
    print(f"Complejidad O(nlogn):Tiempo Lineal")
    xp = [45,88,92,10,28,38,12,3,90]
    xp.sort()
    for n in xp:
        arr.append(f"xp a nivel {n}")
    return arr


#Tiempo Cuadratico: (O(n^2))
def dados2(arr):
    print(f"Complejidad O(n^2):Tiempo Cuadratico")
    lados = (int(input(f"Dame el numero de lados de los dados\n")))
    for i in range (1,lados+1,1):
        for j in range (1,lados+1,1):
            arr.append ((f"{i} {j}"))
    return arr 

#Tiempo Exponencial: (O(2^n))
def pokemonshinyaparece(generacion):
    if generacion == 0:
        return 1
    else:
        return pokemonshinyaparece(generacion-1) + pokemonshinyaparece(generacion-1)

#Tiempo Factorial: (O(n!))
def verpeliculas(n):
    if n == 0:
        return 1
    else:
        contar = 0
        for i in range(n):
            contar += (verpeliculas(n-1))
        return contar

if __name__ == "__main__":
    listaprincipal=[]
    print(f"Los numeros {numerosperfectos(listaprincipal)} Son numeros perfectos\n")
    listaprincipal.clear()
    print(f"El torneo funcionara de la siguiente manera {rondastorneo(listaprincipal)}\n") 
    listaprincipal.clear()
    print(f"Los numeros {multiplosde9(listaprincipal)} Son multiplos de 9\n")
    listaprincipal.clear()
    print(f"Los niveles de XP del jugador seran {niveldexpmenoramayor(listaprincipal)}\n")
    listaprincipal.clear()
    print(f"Las combinaciones posibles de 2 dados son {dados2(listaprincipal)}\n")
    listaprincipal.clear()
    print(f"Complejidad O(2^n):Tiempo Exponencial")
    for gen in range(1,21+1,1):
        print(f"son {gen} de {pokemonshinyaparece(gen)} probabilidades de que aparezcan al mismo tiempo\n")
    listaprincipal.clear()
    print(f"Complejidad O(n!):Tiempo Factorial")
    peli = int(input("Cuantas peliculas vas a ver\n"))
    print(f"Las formas en las que se pueden ver las peliculas son {verpeliculas(peli)}\n")
    