'''
numero = 100
while numero >= 0:
    print(numero)
    numero -= 5

numero1 = int(input("Introduce un número entero: "))
numero2 = int(input("Introduce otro número entero: "))
if numero1 > numero2:
    numero_mayor = numero1
    numero_menor = numero2
else:
    numero_mayor = numero2
    numero_menor = numero1
while numero_menor <= numero_mayor:
    if numero_menor % 2 == 0:
        print(numero_menor)
    numero_menor += 1
    '''
print("S. Sumar\nR. Restar\nD. Dividir\nM. Multiplicar\nP. Potenciar")
opcion = input("Elige una opción: ")
opcion = opcion.upper() 

while True:
    numero1 = int(input("Introduce un número entero: "))
    numero2 = int(input("Introduce otro número entero: "))
    match opcion:
        case "S":
            print("Suma")
            print(f"El resultado de la suma es: {numero1 + numero2}")
        case "R":
            print("Resta")
            print(f"El resultado de la resta es: {numero1 - numero2}")
        case "D":
            print("División")
            if numero2 != 0:
                print(f"El resultado de la división es: {numero1 / numero2}")
            else:
                print("Error: División por cero no permitida.")
        case "M":
            print("Multiplicación")
            print(f"El resultado de la multiplicación es: {numero1 * numero2}")
        case "P":
            print("Potenciación")
            print(f"El resultado de la potenciación es: {numero1 ** numero2}")
        case "E":
            break
        case _:
            print("Modo no válido.")
