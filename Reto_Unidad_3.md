# Problema 1: Control de altitud en ascenso
### Descripcion:
Un avion inicia un ascenso con una altitud determinada y debe alcanzar una altitud objetivo dentro de un tiempo limitado. El piloto controla la potencia, y segun la eleccion, la tasa de ascenso cambia. Si la altitud supera el techo de servicio, aparece una advertencia. El reto consiste en dicidir la potencia adecuada en cada minuto para alcanzar la altitud deseada antes de que termine la simulacion.

# Analisis:
| Variable | Tipo | Rol | Comentario |
| -------- |----- |-----|------------|
|altitud_inicial|float|Entrada|Se pide al usuario, define el punto de partida del avion|
|altitud_objetivo|float|entrada|Altitud que debe alcanzar el avion.|
|techo_servicio|float|Entrada|Altitud maxima permitida antes de advertencia|
|altitud|float|Intermedia/Salida|Se actualiza en cada ciclo con la nueva altitud|
|minuto|int|Control|Variable del bucle `for`, controla los ciclos de simulacion.|
|decision|int|Entrada/Control|Eleccion del usuario sobre la potencia(1, 2, 3).|
|incremento|float|Intermedia|Cantidad de metros que gana el avion por minuto segun la decision.|

# Pseudocodigo:
```
Inicio
    Leer altitud_inicial
    Leer altitud_objetivo
    Leer techo_servicio
    altitud = altitud_inicial

    Para minuto desde 1 hasta 10 hacer
        Mostrar altitud actual
        Mostrar opciones de potencia(1, 2, 3)
        Leer decision 

        Si decision = 1 entonces
            incremento = 100
        Sino si decision = 2 entonces
            incremento = 200
        Sino si decision = 3 entonces
            incremento = 400
        Sino 
            incremento = 0
        FinSi

        altitud = altitud + incremento

        Si altitud >= techo_servicio entonces
            Mostrar advertencia
            Salir del ciclo
        FinSi

        Si altitud >= altitud_objetivo entonces
            Mostrar "El avion alcanzo la altitud objetivo"
            Salir del ciclo
        FinSi
    FinPara

    Si altitud < altitud_objetivo entonces
        mostrar "No se alcanzo la altitud objetivo"
    FinSi

Fin
```
# Prueba de Escritorio:
### Datos de entrada (Ejemplo):
`altitud_inicial = 1500`m<br>
`altitud_objetivo = 3000`m<br>
`techo_servicio = 10000`m<br>
Decisiones por minuto (usuario):`[2, 2, 3, 3, 3]`<br>
donde 1=baja, 2=media, 3=alta.<br>
Incrementos: 1=100m, 2=200m, 3=400m.<br>
Numero maximo de minutos: 10(bucle for 1...10)


|Minuto|Altitud antes(m)|Decision|Incremento(m)|Altitud despues(m)|¿altitud>=techo(m)?|¿altitud>=objetivo?|Accion/Salida|
|------|----------------|--------|-------------|------------------|-------------------|-------------------|-------------|
|1|1500|2|200|1700|No|No|Mostrar altitud, continuar|
|2|1700|2|200|1900|No|No|continuar|
|3|1900|3|400|2300|No|No|continuar|
|4|2300|3|400|2700|No|No|continuar|
|5|2700|3|400|3100|No|Si|Mostrar "¡El avion alcanzo la altitud objetivo! = break(salir del bucle)"|


# Problema 2: Estabilidad en turbulencia
### Descripcion:
Durante el vuelo, el avion atraviesa una zona de turbulencia. En cada segundo, una perturbacion aleatoria modifica el angulo de ataque. Elpiloto debe decidir si corrige el control o no. Si el angulo supera 15°, el avion entra en perdida. El objetivo es atravesar 10 segundos de turbulencias sin perder la estabilidad.

# Analisis:

|Variable| Tipo| Rol|Comentario|
|--------|-----|----|----------|
|`angulo`|float|Intermedia/salida|Ángulo de ataque del avión que cambia cada segundo.|
|`segundo`|int|Control|Variable del bucle `for`, representa el tiempo transcurrido.|
|`perturbacion`|int|Intermedia|Cambio aleatorio generado por la turbulencia.|
|`decision`|int|Entrada/control|Acción del piloto: corregir o no corregir el ángulo.|

# Pseudocodigo:
```
    Inicio
        angulo ← 5

        Para segundo desde 1 hasta 10 hacer
            perturbacion = valor aleatorio entre -3 y 5
            angulo = angulo + perturbacion
            Mostrar angulo actual
            Mostrar opciones: corregir (1) o no corregir (2)
            Leer decision

            Si decision = 1 entonces
                angulo = angulo - 4
            FinSi

            Si angulo > 15 entonces
                Mostrar "El avión entró en pérdida"
                Salir del ciclo
            FinSi
        FinPara

        Si angulo ≤ 15 durante todo el ciclo entonces
            Mostrar "El avión atravesó la turbulencia con éxito"
        FinSi
    Fin
```
# Prueba de escritorio:
Para la prueba tomo una secuencia de perturbaciones fija:
perturbaciones = [2, 4, 5, 3, -2, 5, 1, -3, 4, 2] (valores en grados)

Se haran dos escenarios: A) el piloto corrige cuando conviene → atraviesa la turbulencia.<br
> B) el piloto no corrige a tiempo → entra en pérdida.
### Escenario A Éxito: (decisiones del piloto: 1=corregir, 2=no)

Decisiones: [2, 2, 1, 2, 2, 1, 2, 2, 1, 2] (corrige en segundos 3, 6 y 9)

|Segundo|Perturbación (°)|Ángulo antes (°)|Ángulo tras perturbación (°)|    Decision|Ángulo tras corrección (°)|¿ángulo > 15?| Acción|
|------|------|-----|-----|-----|-----|-----|-----|
|1|+2 |5|7|2 (no corregir)|7|7 > 15 ? No|continuar|
|2|+4|7|11|2|11|No|continuar|
|3|+5|11|16|1 (corregir)|12 (16 − 4)|12 > 15 ? No|continuar|
|4|+3|12|15|2|15|15 > 15 ? No (igual a 15 es seguro)|continuar|
|5|−2|15|13|2|13|No|continuar|
|6|+5|13|18|1 (corregir)|14|No|continuar|
|7|+1|14|15|2|15|No|continuar|
|8|−3|15|12|2|12|No|continuar|
|9|+4|12|16|1 (corregir)|12 |No|continuar|
|10|+2|12|14|2|14|No| fin del bucle = éxito |

### Escenario B Falla: (piloto no corrige a tiempo)

Decisiones: [2, 2, 2, ...] (nunca corrige)

|Segundo|Perturbación (°)|Ángulo antes|Tras perturbación|Decision|Tras corrección|¿ángulo > 15?|Acción|
|------|------|------|------|------|------|------|------|
|1|+2|5|7|2|7|No|continuar|
|2|+4|7|11|2|11|No|continuar|
|3|+5|11|16|2|16|16 > 15 = Sí|Imprimir pérdida y break|

# Problema #3:Alcance de un planeador

#### Descripción:
Un planeador inicia su descenso desde cierta altitud con una relación de planeo (L/D). El piloto decide en cada ciclo si mantiene la velocidad o acelera, lo que afecta la pérdida de altitud y la distancia recorrida. El objetivo es alcanzar un aeropuerto ubicado a cierta distancia antes de quedarse sin altitud.

# Analisis:

|Variable|Tipo|Rol|Comentario|
|--------|----|---|----------|
|`altitud_inicial`|float|Entrada|Altitud inicial desde la que empieza el planeador.|
|`distancia_objetivo`|float|Entrada|Distancia al aeropuerto en kilómetros.|
|`LD`|float|Entrada|Relación de planeo (L/D), eficiencia del planeador.|
|`velocidad`|float|Intermedia|Velocidad del planeador en m/s, puede aumentar.|
|`altitud`|float|Intermedia/salida|Altitud restante del planeador durante la simulación.|
|`distancia_recorrida`|float|Intermedia/salida|Acumula la distancia recorrida hasta alcanzar o no el aeropuerto. |
|`distancia`|float|Intermedia|Distancia parcial recorrida en cada ciclo.|
|`decision`|int|Entrada/control|Elección del piloto: mantener o aumentar velocidad.|

# Pseudocodigo:
```
    Inicio
        Leer altitud_inicial
        Leer distancia_objetivo
        Leer LD
        velocidad = 50
        distancia_recorrida = 0
        altitud = altitud_inicial

        Mientras altitud > 0 Y distancia_recorrida < distancia_objetivo hacer
            Mostrar altitud y distancia recorrida
            Mostrar opciones: mantener velocidad (1) o acelerar (2)
            Leer decision

            Si decision = 2 entonces
                velocidad = velocidad + 10
                altitud = altitud - 150
            Sino
                altitud = altitud - 100
            FinSi

            distancia = velocidad × LD × 0.1
            distancia_recorrida ← distancia_recorrida + distancia
        FinMientras

        Si distancia_recorrida ≥ distancia_objetivo entonces
            Mostrar "El planeador llegó al aeropuerto"
        Sino
            Mostrar "El planeador se quedó sin altitud y no llegó"
        FinSi
    Fin
```

# Prueba de escritorio:
Haré dos escenarios: A) objetivo cercano = llega<br>. B) objetivo lejano = no llega. 
### Escenario A Exito: (Objetivo = 1km)
Entradas:

altitud_inicial = 1500 m

distancia_objetivo = 1.0 km = objetivo_m = 1000 m

LD = 20

velocidad inicial = 50 m/s

decisiones (mantener siempre): todos 1 (mantener)

Cálculo de distancia parcial (cada ciclo si mantener):
distancia = velocidad * LD * 0.1 = 50 * 20 * 0.1 = 100 m por ciclo. Altitud pierde 100 m por ciclo.

|Ciclo|Vel. antes(m/s)|Decision|Distancia parcial(m)|Dist. acumulada(m)|Altitud antes(m)|Altitud después(m)|¿alcanzó objetivo?|
|----|----|----|----|----|----|----|----|
|1 |50|mantener|100|100|1500|1400|100 ≥ 1000 ? No|
|2 |50|mantener|100|200|1400|1300|No|
|3 |50|mantener|100|300|1300|1200|No|
|4 |50|mantener|100|400|1200|1100|No|
|5 |50|mantener|100|500|1100|1000|No|
|6 |50|mantener|100|600|1000|900 |No|
|7 |50|mantener|100|700|900 |800 |No|
|8 |50|mantener|100|800|800 |700 |No|
|9 |50|mantener|100|900|700 |600 |No|
|10|50|mantener|100|1000|600|500 |1000 ≥ 1000 ? Sí = salir|

### Escenario B Falla: (Objetivo = 5km)

Entradas:

altitud_inicial = 1500 m

distancia_objetivo = 5.0 km = 5000 m

LD = 15

velocidad = 50 m/s

decisiones: mantener siempre

Distancia parcial por ciclo: 50 * 15 * 0.1 = 75 m
Altitud pierde 100 m por ciclo si mantiene.

Calculamos 15 ciclos (hasta altitud 0):

|Ciclo|Dist. parcial (m)|Dist. acumulada (m)|Altitud después (m)|
|-----|-----------------|-------------------|-------------------|
|   1 |              75 |                75 |              1400 |
|   2 |              75 |               150 |              1300 |
|   3 |              75 |               225 |              1200 |
|   4 |              75 |               300 |              1100 |
|   5 |              75 |               375 |              1000 |
|   6 |              75 |               450 |               900 |
|   7 |              75 |               525 |               800 |
|   8 |              75 |               600 |               700 |
|   9 |              75 |               675 |               600 |
|  10 |              75 |               750 |               500 |
|  11 |              75 |               825 |               400 |
|  12 |              75 |               900 |               300 |
|  13 |              75 |               975 |               200 |
|  14 |              75 |              1050 |               100 |
|  15 |              75 |          **1125** |0 = `altitud <= 0` |

