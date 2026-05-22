import numpy as np

#leer csv
datosjugadores = np.genfromtxt(
    "jugadores_futbol.csv",
    delimiter = ",",
    dtype = None,
    encoding = "utf-8",
    names = True
)

print(datosjugadores)

#top 5 jugadores

jugadoresordenados = np.sort(
    datosjugadores,
    order = "Goles"
)

top5 = jugadoresordenados[-5:]
print(f"Top 5 de goleadores: {top5}")

input()
#promedio edad

promedioEdad = np.mean(datosjugadores["Edad"])


print(f"Promedio de edad: \n{promedioEdad}")

#Top 10 jugadores mas caros

jugadoresCaros = np.sort(
    datosjugadores,
    order = "ValorMercado"
)

top10 = jugadoresCaros[-10:]
print(f"Top 10 mas caros: \n{top10}")

input()

np.savetxt(
    "Jugadores_Mas_Caros.csv",
    top10,
    delimiter = ",",
    fmt = "%s",
    header = "ID,JUGADOR,EQUIPO,POSICION,EDAD,PARTIDOS,GOLES,ASISTENCIA,VALORMERCADO"
)

input()

#EJERCICIO
#Total de goles
#promeedio de goles
#maxima cantidad de goles

Total_de_Goles = np.sum(datosjugadores["Goles"])
print(f"Total de goles: {Total_de_Goles}")
Promedio_de_Goles = np.mean(Total_de_Goles)
print(f"Promedio de Goles: {Promedio_de_Goles}")
Max_goles = np.max(datosjugadores["Goles"])
print(f"Maxima Cantidad de Goles: {Max_goles}")
