'''
variables de entrada
numero           int
vartiables de salida
divisores        int
'''
numero = int(input("Ingrese un numero entero mayor que 1: "))
contador = 0
for i in range (1, numero+1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print(f"{numero} es primo")
else:
    print("los divisores de ese numero son: ")
    for i in range (1, numero+1):
        if numero % i == 0:
            print(i)
