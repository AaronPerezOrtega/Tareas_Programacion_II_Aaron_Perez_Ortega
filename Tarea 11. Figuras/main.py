from modelos.circulo import Circulo
from modelos.triangulo import Triangulo
from modelos.cuadrado import Cuadrado

#Se crea un  circulo de radio 4
circulo = Circulo(4)

#Se imprimen su Area y su perimetro
print(f"Area del circulo: {circulo.area():.4f}")
print(f"Perimetro del circulo: {circulo.perimetro():.4f}")

#Se crea un  cuadrado con sus lados de 5
cuadrado = Cuadrado(5)

#Se imprimen su Area y su perimetro
print(f"Área del cuadrado: {cuadrado.area()}")
print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")

#Se crea un triangulo de base 6 y altura 3
triangulo = Triangulo(6, 3)

#Se añaden sus lados, y base se toma como uno de sus lados
triangulo.lados(5)
triangulo.lados(5)

#Se imprimen su Area y su perimetro
print(f"Área del triángulo: {triangulo.area():.4f}")
print(f"Perímetro del triángulo: {triangulo.perimetro()}")