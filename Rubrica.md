## Tabla 1. Checklist de requisitos del reto (por problema)

|Requisito|Cumple 2/Parcialmente 1/No cumple 0|Evidencia(sección/tablas)|
|---------|-----------------------------------|-------------------------|
|**Contexto aeronáutico claro y relevante**| 2 |Descripciones de problemas: <br>- Problema 1: ascenso a altitud objetivo. <br>- Problema 2: turbulencias que afectan el ángulo de ataque. <br>- Problema 3: planeador que busca llegar a un aeropuerto con L/D.|
|**Clara definición y clasificación de las variables (entrada, salida, control, intermedias)**| 2 |Tablas de análisis de variables (hechas para cada problema: altitud, objetivo, perturbación, LD, velocidad, etc.).|
|**Clara definición de las constantes**| 2 |Tablas de análisis + código: tasas de ascenso fijas (100, 200, 400 m/min), velocidad inicial del planeador = 50 m/s, corrección de ángulo = 4°.|
|**Ecuación que relaciona adecuadamente las variables del problema**| 2 | Pseudocódigos y pruebas de escritorio: <br>- Ascenso: `altitud = altitud + incremento`. <br>- Turbulencia: `ángulo = ángulo + perturbación - corrección`. <br>- Planeador: `distancia = velocidad * (L/D) * 0.1`.|
|**No es solo cálculo directo**| 2 |Descripción + código + pruebas: todos los problemas incluyen decisiones del usuario, simulación por ciclos y condiciones de paro.|
|**Al menos un bucle (variable de control, condición de parada)**| 2 | Pseudocódigo y pruebas de escritorio: <br>- Problema 1: `for minuto in range(1,11)`. <br>- Problema 2: `for segundo in range(1,11)`. <br>- Problema 3: `while altitud > 0 and distancia < objetivo`.|
|**Al menos una sentencia condicional significativa**| 2 |Código y pruebas de escritorio: <br>- Ascenso: `if altitud >= objetivo` o `if altitud >= techo`. <br>- Turbulencia: `if angulo > 15`. <br>- Planeador: `if distancia_recorrida >= distancia_objetivo`.|
|**Menú repetitivo hasta “Salir”**| 2 |Código principal: función `menu()` con `while opcion != 4`.|
|**Sin listas, diccionarios, tuplas ni sets**| 2 |Código validado: solo variables simples (`float`, `int`), sin estructuras avanzadas.|
| **Declaración de uso de IA (si aplica)**| 2 | Se utilizo la inteligencia artificial para ayudar al planteamiento de los problemas y como guia para presentar un trabajo adecuado, como para corregir errores y formalizar los terminos, variables y estructura del codigo.|
