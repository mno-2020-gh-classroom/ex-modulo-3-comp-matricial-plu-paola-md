# Factorización PLU: Cómputo Matricial

**Integrantes del equipo**

| # | Alumno    |        Rol         |      User github       |
|---|-----------|--------------------|------------------------|
| 1 | Rafael    |    Project Manager |      123972            |
| 2 | Paola     |    Programadora    |      paola-md          |
| 3 | Sebastián |    Programador     |      C1587S            |
| 4 | Alfie     |    Programador     |      gonzalezalfie     |
| 5 | Maggie    | Revisión de código |      maggiemusa        |  
| 6 | Karla     | Revisión de código |      alpika19186       |
| 7 | Yalidt    | Revisión de código |      Yalidt            |

## Factorización PLU simple

#Escribir de manera teórica en qué consiste la factorización PLU simple

### Programación del código simple en Python

* Requirements: Importar los siquientes paquetes: numpy as np , timeit, matplotlib.pyplot as plt

* Breve descripción del script: Factorización_PLU.py

### Pruebas del código simple en Python

* Corroborar el cálculo de P,L,U y X:

Este script nos ayuda a verificar que los valores obtenidos para P,L,U y X están bien calculados usando scipy para comprobar. 

1. Generamos matrices de distinta dimensión de forma aleatoria
2. Obtenemos los valores P, L y U para las matrices llamando al script Factorización_PLU.py. Si U contiene un cero en la diagonal, la matriz es singular y se detiene. Si no, continúa con la solución.
3. Comparamos los valores obtenidos de P, L y U con los obtenidos en scipy para matrices pequeñas y medianas (10^2 o 10^3).
4. Si las matrices son iguales, cotinuamos resolviendo para X usando el script Factorización_PLU.py.
5. Comparamos los valores obtenidos de X los obtenidos en scipy para matrices pequeñas y medianas (10^2 o 10^3).

* Evaluación del tiempo de ejecución y memoria al variar la dimensión:

Este script nos ayuda a verificar el tiempo y memoria utilizados al cambiar las dimensiones de las matrices.

1. Generamos matrices de distinta dimensión de forma aleatoria
2. Obtenemos los valores P, L, U y X para las matrices llamando al script Factorización_PLU.py. Si U contiene un cero en la diagonal, la matriz es singular y se detiene. Si no, continúa con la solución.
3. Medimos el tiempo de ejecución y la memoria y se exportan los valores a un data frame para generar gráficas con ellos.
5. Graficamos los distintos valores de tiempo, memoria etc dependiendo el tamaño de la matriz.

## Factorización PLU por bloques

#Escribir de manera teórica en qué consiste la factorización PLU por bloques

### Programación del código por bloques en Python

### Reporte de resultados

#Mostrar los principales resultados al variar la dimensión, datos de entrada de A, datos de entrada de b contra el tiempo, la memoria etc.

#Figura 1. Comparación de la dimensión de la matriz contra el tiempo promedio de ejecución

#Figura 2. Comparación de la dimensión de la matriz contra el uso de memoria

#Figura 3. Comparación de la dimensión de la matriz contra el error relativo
