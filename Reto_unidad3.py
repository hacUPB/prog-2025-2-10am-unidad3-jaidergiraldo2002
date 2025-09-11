import random
# ----------------------------
# PROBLEMA 1: ASCENSO Y ALTITUD
# ----------------------------
def problema_altitud():
   print("\n--- Simulación de Ascenso y Control de Altitud ---")
   altitud = float(input("Ingrese altitud inicial (m): "))
   objetivo = float(input("Ingrese altitud objetivo (m): "))
   techo = float(input("Ingrese techo de servicio del avión (m): "))
   for minuto in range(1, 11):
       print(f"\nMinuto {minuto} | Altitud actual: {altitud:.2f} m")
       print("1. Potencia baja\n2. Potencia media\n3. Potencia alta")
       decision = int(input("Seleccione potencia: "))
       if decision == 1:
           incremento = 100
       elif decision == 2:
           incremento = 200
       elif decision == 3:
           incremento = 400
       else:
           incremento = 0
       altitud += incremento
       if altitud >= techo:
           print("Advertencia: ha alcanzado el techo de servicio.")
           break
       if altitud >= objetivo:
           print(" ¡El avión alcanzó la altitud objetivo con éxito!")
           break
   else:
       print("No se alcanzó la altitud objetivo en el tiempo dado.")
# ----------------------------
# PROBLEMA 2: ESTABILIDAD EN TURBULENCIA
# ----------------------------
def problema_turbulencia():
   print("\n--- Simulación de Estabilidad en Turbulencia ---")
   angulo = 5  # ángulo inicial seguro
   for segundo in range(1, 11):
       perturbacion = random.randint(-3, 5)  # turbulencia aleatoria
       angulo += perturbacion
       print(f"\nSegundo {segundo} | Ángulo actual: {angulo}°")
       print("1. Corregir control (reducir ángulo)\n2. No hacer nada")
       decision = int(input("Elija acción: "))
       if decision == 1:
           angulo -= 4  # corrección del piloto
       if angulo > 15:  # condición de pérdida
           print("El avión entró en pérdida por exceso de ángulo de ataque!")
           break
   else:
       print("El avión atravesó la turbulencia sin entrar en pérdida.")
# ----------------------------
# PROBLEMA 3: ALCANCE DE PLANEADOR
# ----------------------------
def problema_planeador():
   print("\n--- Simulación del Alcance de un Planeador ---")
   altitud = float(input("Ingrese altitud inicial (m): "))
   distancia_objetivo = float(input("Ingrese distancia al aeropuerto (km): "))
   LD = float(input("Ingrese relación de planeo (L/D): "))
   velocidad = 50  # m/s inicial
   distancia_recorrida = 0
   while altitud > 0 and distancia_recorrida < distancia_objetivo * 1000:
       print(f"\nAltitud: {altitud:.2f} m | Distancia recorrida: {distancia_recorrida/1000:.2f} km")
       print("1. Mantener velocidad\n2. Aumentar velocidad (+10 m/s)")
       decision = int(input("Elija acción: "))
       if decision == 2:
           velocidad += 10
           altitud -= 150  # más velocidad = más pérdida de altitud
       else:
           altitud -= 100  # descenso normal
       distancia = velocidad * LD * 0.1  # cálculo directo sin función
       distancia_recorrida += distancia
   if distancia_recorrida >= distancia_objetivo * 1000:
       print("✈ ¡El planeador llegó al aeropuerto!")
   else:
       print("El planeador se quedó sin altitud y no llegó.")
# ----------------------------
# MENÚ PRINCIPAL
# ----------------------------
def menu():
   opcion = 0
   while opcion != 4:
       print("\n===== MENÚ PRINCIPAL =====")
       print("1. Problema 1: Control de altitud en ascenso")
       print("2. Problema 2: Estabilidad en turbulencia")
       print("3. Problema 3: Alcance de un planeador")
       print("4. Salir")
       opcion = int(input("Elija una opción: "))
       if opcion == 1:
           problema_altitud()
       elif opcion == 2:
           problema_turbulencia()
       elif opcion == 3:
           problema_planeador()
       elif opcion == 4:
           print("Saliendo del programa...")
       else:
           print("Opción no válida. Intente de nuevo.")
# Ejecutar menú
menu()