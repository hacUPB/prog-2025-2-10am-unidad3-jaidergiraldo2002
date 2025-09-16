def primo(numero:int):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1 #cont = cont + 1
    if cont == 2:
        print(f"{numero} es primo")
    else:
        print(f"Los divisores de {numero} son:")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i)
 
def fibonacci(valor:int):
    if valor <= 0:
        print("Por favor, ingrese un número entero positivo.")
    elif valor == 1:
        print("Serie de Fibonacci")
        print(0)
    else:
        a = 0
        b = 1
        contador = 2
        print("Serie de Fibonacci")
        print(a)
        print(b)
       
        while contador < valor:
            siguiente = a + b
            print(siguiente)
            a = b
            b = siguiente
            contador += 1
 
def tabla(numero:int):
    cont = 1
    while cont <= 15:
        res = cont * numero
        print(f"{numero} x {cont} = {res}")
        cont += 1

def menu():
    print("Seleccione una opción:")
    print("1. Verificar si un número es primo")
    print("2. Generar la serie de Fibonacci")
    print("3. Mostrar la tabla de multiplicar")
    print("4. Salir")
    opcion = int(input("Ingrese su opción (1-4): "))
    return opcion

