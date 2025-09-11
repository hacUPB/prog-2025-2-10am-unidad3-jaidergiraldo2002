## Tabla 1. Checklist de requisitos del reto (por problema)

| Requisito | Cumple 2 <br>Parcialmente  <br>1 No cumple   0 | Evidencia (página/tabla/figura/sección) |
| --------- | -------------------------------------- | --------------------------------------- |
| Contexto aeronáutico claro y relevante | 2 |Problema 1: "Durante el ascenso, el avion  debe mantener una tasa de ascenso adecuada para llegar a su altitud objetivo". <br>Problema 2: "El avion atraviesa una zona con turbulencias que afectan su angulo de ataque". <br>Problema 3: "Un planeador desciende desde cierta altitud con un coeficiente de planeo (L/D)." |
| Clara definición y clasificación de las variables de entrada, salida, de control e intermedias | 2 | Variables de entrada: altitud inicial, altitud objetivo, techo de servicio, distancia al aeropuerto, relacion L/D. <br>Variables de salida: altitud alcanzada, angulo final, distancia recorrida. <br>Variables de control: minuto, segundo, ciclos del bucle. <br>Intermedias: incremento de altitud, perturbacion, distancia parcial. |
| Clara definición de las constantes que se utilizan en el problema | 2 | Constantes fijadas en el codigo: velocidad inicial =50m/s(Problema 3), angulo inicial = 5°(Problema 2), tasas de ascensos fijas( 100,200,400 m/min en Problema 1). |
| Ecuación que relaciona adecuadamente las variables del problema | 2 | Problema 1: Altitud nueva = altitud + incremento segun potencia. <br>Problema2: Angulo nuevo = Angulo + Perturbacion - Correccion. <br>Problema 3: Distancia recorrida = velocidad x (L/D) x 0.1, con descenso de altitud en cada ciclo. |
| No es solo cálculo directo | 2 | Cada problema es una simulacion interactiva con decisiones del usuario, bucles y condiciones , no una sola formula. |
| Al menos un bucle (variable de control, condición de parada) | 2 | Problema 1: `for minuto in range(1,11)`<br>Problema 2: `for segundo in range (1,11)`<br>Problema 3: `while altitud > 0 and distancia_recorrida < distancia objetivo` |
| Al menos una sentencia condicional significativa | 2 | Problema 1: `if altitud >= objetivo`/`if altitud >= techo`<br>Problema 2: `if angulo > 15` (Perdida).<br>Problema 3:`if distancia_recorrida >= distancia_objetivo`. |
| Menú repetitivo hasta “Salir” | 2 | Funcion `menu()` con `while opcion != 4`. |
| Sin listas, diccionarios, tuplas ni sets | 2 | Todo el codigo usa variables simples (`float`, `int`) |
| Declaración de uso de IA (si aplica) | 2 | Se uso ChatGPT para el planteamiento de los ejercicios y como guia de referencia de como establecer un randomizador |