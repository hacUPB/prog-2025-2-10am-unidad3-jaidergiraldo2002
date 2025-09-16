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
`techo_servicio = 1000`m<br>
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

