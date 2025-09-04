n = -1
while n <= 0: 
    n = int(input("Ingrese un numero positivo: "))
    acum = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            acum += i
    print(f"La suma de los numeros pares es: {acum}")
