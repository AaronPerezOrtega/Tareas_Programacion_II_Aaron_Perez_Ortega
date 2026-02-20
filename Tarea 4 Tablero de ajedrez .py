import datetime
def ajedrez(n):
    if n == 0:
        return n+1
    else:
        res = 2 * ajedrez(n-1)
        return res

def main():
    for potencia in range(0, 65, 1):
        print(f"potencia {potencia} casilla: {ajedrez(potencia)}")

if __name__ == '__main__':
    print(f"La hora y fecha de inicio es: {datetime.datetime.now()}")
    main()
    print(f"La hora y fecha de fin es: {datetime.datetime.now()}")
    int(input(""))
