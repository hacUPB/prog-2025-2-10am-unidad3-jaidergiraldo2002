'''Problema 1(ascenso y altitud):
Durante un ascenso, el avion debe mantener una tasa de ascenso adecuada para llegar a su altitud objetivo.
El usuario debe fijar una altitud final y en cada ciclo decide si aumentar, disminuir o mantener la potencia.
La tasa de ascenso cambia segun la potencia y se recalcula la altitud alcanzada.
El programa termina cuando se alcanza la altitud deseada o cuando acaba el tiempo maximo.
'''

def problema_altitud():
    print("n\--- Simulacion de Ascenso y Control de Altitud---")
    altitud = float(input("Ingrese la altitud inicial (m): "))
    objetivo = float(input("ingrese la altitud objetivo(m)"))
    techo = float(input("Ingrese techo de servicio del avion(m): "))

    for minuto in range (1,11):
        print(f"\nMinuto {minuto} | Altitud actual: {altitud:.2f}m")
        print