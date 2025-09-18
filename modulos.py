'''
import mod_funciones

numero = int(input("Ingrese un número entero mayor que 1: "))
mod_funciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
mod_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones.tabla(multiplicando)
'''
from mod_funciones import *

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("Verificar si un número es primo")
                num = int(input("Ingrese un número entero mayor que 1: "))
                primo(num)
            case 2:
                print("Imprimir la serie de Fibonacci")
                val = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
                fibonacci(val)
            case 3:
                print("Imprimir la tabla de multiplicar")
                num = int(input("Ingrese el número entero: "))
                tabla(num)
            case 4:
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
    