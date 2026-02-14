nu1 = int(input(f"Dame el primer numero \n"))
nu2 = int(input(f"Dame el segundo numero \n"))
nu3 = int(input(f"Dame el tercer numero \n"))
res = nu1+nu2+nu3
print (f"El resultado de la suma es:", res)
prom = res/3
print (f"El promedio es:", prom)
if nu1 >= nu2 and nu1 >= nu3:
    print (f"El numero mayor es el primero que es:", nu1)
elif nu2 >= nu1 and nu2 >= nu3:
    print (f"El numero mayor es el segundo que es:", nu2)
elif nu3 >= nu1 and nu3 >= nu2:
    print (f"El numero mayor es el tercero que es:", nu3)