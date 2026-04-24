from modelos.circulo import Circulo
from modelos.triangulo import Triangulo
from modelos.cuadrado import Cuadrado

circulos = []
cuadrados = []
triangulos = []

def triangulo():
    x = int(input("Dame la Base\n"))
    y = int(input("Dame la Altura\n"))
    triangulo = Triangulo(x,y)
    for i in range (2):
        z = int(input("Dame un lado del triangulo\n"))
        triangulo.lados(z)
    triangulos.append(triangulo)

def cuadrado():
    x = int(input("Dame el lado\n"))
    cuadrado = Cuadrado(x)
    cuadrados.append(cuadrado)
    
def circulo():
    x = int(input("Dame el radio\n"))
    circulo = Circulo(x)
    circulos.append(circulo)

def main():
    while True:
        try:
            menu = int(input(f"__________Menu_______________" 
                    f"\n1.- Crea una figura \n2.- Mostrar figuras\n"
                    f"3.- Calcular Area\n"
                    f"4.- Calcular Perimetro \n5.- Salir\n"))
            print("")
            if menu == 1: 
                submenu = int(input(f"1.- Crear un triangulo\n"
                                    f"2.- Crear un Cuadrado\n"
                                    f"3.- Crear un Circulo\n"
                                    f"4.- regresar\n"))
                print("")
                if submenu == 1:
                    triangulo()
                elif submenu == 2:
                    cuadrado()
                elif submenu == 3:
                    circulo()
                elif submenu == 4:
                    print(f"Regresando")
                else:
                    print("Opcion invalida")
            
            elif menu == 2:
                print("Figuras:4")
                print("\nTriangulos")
                if len(triangulos) == 0:
                    pass
                else:
                    for i, t in enumerate(triangulos, 1):
                        print(f"Triángulo {i}: Base={t.obtener_base()}, Altura={t.obtener_altura()}, Lado 1={t.obtener_lado(0)} Lado 2={t.obtener_lado(1)}")

                print("\nCuadrados")
                if len(cuadrados) == 0:
                    pass
                else:
                    for i, c in enumerate(cuadrados, 1):
                        print(f"Cuadrado {i}: Lado={c.obtener_lado()}")

                print("\nCirculos")
                if len(circulos) == 0:
                    pass
                else:
                    for i, c in enumerate(circulos, 1):
                        print(f"Círculo {i}: Radio={c.obtener_radio()}")

            elif menu == 3:
                print("Areas:")
                print("\nTriangulos")
                if len(triangulos) == 0:
                    pass
                else:
                    for i, t in enumerate(triangulos, 1):
                        print(f"Triángulo {i}: Area= {t.area():.4f}")

                print("\nCuadrados")
                if len(cuadrados) == 0:
                    pass
                else:
                    for i, c in enumerate(cuadrados, 1):
                        print(f"Cuadrado {i}: Area= {c.area()}")

                print("\nCirculos")
                if len(circulos) == 0:
                    pass
                else:
                    for i, c in enumerate(circulos, 1):
                        print(f"Circulo {i}: Area= {c.area():.4f}")
                print("")

            elif menu == 4:
                print("Perimetros:")
                print("\nTriangulos")
                if len(triangulos) == 0:
                    pass
                else:
                    for i, t in enumerate(triangulos, 1):
                        print(f"Triángulo {i}: Perimetro= {t.perimetro()}")

                print("\nCuadrados")
                if len(cuadrados) == 0:
                    pass
                else:
                    for i, c in enumerate(cuadrados, 1):
                        print(f"Triángulo {i}: Perimetro= {c.perimetro()}")

                print("\nCirculos")
                if len(circulos) == 0:
                    pass
                else:
                    for i, c in enumerate(circulos, 1):
                        print(f"Triángulo {i}: Perimetro= {c.perimetro():.4f}")
                print("")

            elif menu == 5:
                print("Gracias por Usar :D")
                break

            else:
                print("Opción inválida")

        except ValueError:
            print("Opcion no valida")    

if __name__ == "__main__":
    main()