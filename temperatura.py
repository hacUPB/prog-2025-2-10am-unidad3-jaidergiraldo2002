'''
Variables de entrada:
Nombre         Tipo
opcion         str
temperatura    float

Variables de salida:
Nombre         Tipo
conversion     float

Variable de control
opcion
'''

opcion = "F"            #Asigno un valor diferente de Q
while opcion != "Q":
    opcion = input("F. Fahrenheit a Celcius\nC. Celcius a Fahrenheit\nQ. Salir\n").upper()
    temperatura = float(input("Ingrese la temperatura a convertir: "))
    match opcion:
        case "F":
            conversion = (temperatura - 32)*(5/9)
            print(f"{temperatura}°F = {conversion}°C")
        case "C":
            conversion = (temperatura* 9 / 5) + 32
            print(f"{temperatura}°C = {conversion}°F")
        case "Q":
            print("Saliendo del programa...")
        case _:
            print("Opcion no valida")
        