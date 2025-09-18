numero = int(input("ingrese el numero de terminos de la serie: "))
if numero <= 0:
    print("Por favor ingrese un numero entero positivo.")
elif numero == 1:
    print("Serie de fibonacci: ")
    print(0)
else:
    a = 0
    b = 1
    contador = 2
    print("Serie de Fibonacci: ")
    print(a)
    print(b)

    while contador < numero:
        siguiente = a + b
        print(siguiente)
        a = b
        b = siguiente
        contador += 1
        