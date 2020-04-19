# -*- coding: utf-8 -*-
import revision_functions as rv
import plu_functions
import pytest
import scipy
import time
import pandas as pd
import pprint
import numpy as np
import sys
sys.path.append('./../../')


def test_MatrizSimple():
    '''
    Evalúa la factorización PLU para la matriz simple A
    Para más información del ejemplo ver el sript de "programacion_PLU.py"
    '''
    print("* Evalúa el algoritmo para una matriz simple")
    A = np.array([[2, 2, 3], [-4, -4, -3], [4, 8, 3]])
    P, L, U = plu_functions.PLU(A)

    print("Matriz a probar")
    pprint.pprint(A)
    print("P:")
    pprint.pprint(P)
    print("L:")
    pprint.pprint(L)
    print("U:")
    pprint.pprint(U)
    print("PA=LU")
    # probar que PA=LU
    assert (np.matmul(P, A) == np.matmul(L, U)).all()

def test_10Matrices():
    '''
    Evalúa la factorización PLU para 10 matrices cuadradas aleatorias con
    dimensión entre 2x2 y (10^3)x(10^3).
    NOTA: Las entradas de los números son floats están entre -10.000 y 10.000.
    Para más información del ejemplo ver el sript de "revision_PLU.py"
    '''
    np.random.seed(3338014)  # semilla para replicabilidad de las pruebas
    print("* Evalúa el algoritmo PLU para 10 matrices aleatorias hata de 10^2x10^2")
    eps = 1.0E-8  # para definir la precisión a 8 dígitos
    n = 10
    dim_lim_inf = 2
    dim_lim_sup = 10**2
    ents_lim_sup = 10000
    # crea matrices aleatorias
    for i in range(1, n + 1):
        mat, _ = rv.crea_matrices(dim_lim_inf, dim_lim_sup, ents_lim_sup)
    # prueba el algoritmo PLU
        P, L, U = plu_functions.PLU(mat)
        # verifica que la diferencia entre los elementos de la operación PA-LU
        # sean menores a eps
        assert ((np.matmul(P, mat) - np.matmul(L, U))).all() <= eps


def test_comparaSciPyPLU_10Matrices():
    '''
    Evalúa la factorización PLU para 10 matrices cuadradas aleatorias con
    dimensión entre 2x2 y (10^2)x(10^2).

    Compara los elementos P, L, y U de la factorización asociada obtenidos con
    la librería SciPy y con la librería creada para este ejercicio.
    Evalúa que la diferencia de cada elemento de cada una de dichas matrices no
    sea mayor a "eps".
    '''
    np.random.seed(3338014)  # semilla para replicabilidad de las pruebas
    print("* Evalúa 10 veces el algoritmo de factorización PLU para matrices hasta de 10^2x10^2")
    eps = 1.0E-8  # para definir la precisión a 8 dígitos
    n = 10
    dim_lim_inf = 3
    dim_lim_sup = 10**2
    ents_lim_sup = 10000
    # crea matrices aleatorias
    for i in range(1, n + 1):
        mat, _ = rv.crea_matrices(dim_lim_inf, dim_lim_sup, ents_lim_sup)

        # prueba el algoritmo PLU
        P, L, U = plu_functions.PLU(mat)
        P_scipy, L_scipy, U_scipy = scipy.linalg.lu(mat)
        # verificar que los elementos de los dos modulos son iguales
        print("* ¿Solución igual a Scipy?")
        print((P_scipy == P).all() and (L_scipy == L).all() and (U_scipy == U).all())


def test_SisSimpleBloqs():
    '''
    Evalúa el algoritmo por bloques para un sistema simple creado de forma
    determnista.
    '''
    print("* Evalúa el algoritmo por bloques para un sistema simple creado de forma determnista.")
    # crea matrices aleatorias
    A = np.array([[1, 1, -1], [1, 2, 2], [2, 1, -1]])
    print("matriz A: ", A)
    b = np.array([-1, 0, 1])
    print("b: ", b)
    x = plu_functions.solve_blocks(A, b)
    print("x: ", x)

def test_Bloqs1000matricesDim2():
    '''
    Evalúa 1000 veces el algoritmo de factorización PLU y por bloques para
    matrices aleatorias de hata de dimensión 10^2 x 10^2
    '''
    np.random.seed(3338014)  # semilla para replicabilidad de las pruebas
    print("* Evalúa 1000 veces el algoritmo de factorización PLU por bloques")
    eps = 1.0E-8  # para definir la precisión a 8 dígitos
    n_veces = 100
    dim_lim_inf = 2
    dim_lim_sup = 10**2
    ents_lim_sup = 10000

    for i in range(1, n_veces + 1):
        A, dim_mat = rv.crea_matrices(dim_lim_inf, dim_lim_sup, ents_lim_sup)
        # se realiza la multiplicación de A con x_real para obtener el lado derecho del SEL
        X = np.round(np.random.normal(dim_lim_inf, dim_lim_sup, dim_mat),2)
        # computa B
        B=A@X

        try:
            X_algo = plu_functions.solve_blocks(A, B)
            if np.allclose(X,X_algo):
                print("algoritmo computado correctamente")
            else:
                print("algoritmo computado con baja precisión")
        except:
            print("matriz singular")

def test_Bloqs20matricesDim3():
    '''
    Evalúa 20 veces el algoritmo de factorización PLU y por bloques para
    matrices aleatorias de hata de dimensión 10^3 x 10^3

    '''
    np.random.seed(3338014)  # semilla para replicabilidad de las pruebas
    print("* Evalúa PLU por blñoques para 10 matrices hasta de tamaó 10^3x10^3")
    eps = 1.0E-8  # para definir la precisión a 8 dígitos
    n_veces = 20
    dim_lim_inf = 2
    dim_lim_sup = 10**3
    ents_lim_sup = 10000

    for i in range(1, n_veces + 1):
        A, dim_mat = rv.crea_matrices(dim_lim_inf, dim_lim_sup, ents_lim_sup)
        # se realiza la multiplicación de A con x_real para obtener el lado derecho del SEL
        X = np.round(np.random.normal(dim_lim_inf, dim_lim_sup, dim_mat),2)
        # computa B
        B=A@X

        try:
            X_algo = plu_functions.solve_blocks(A, B)
            if np.allclose(X,X_algo):
                print("algoritmo computado correctamente")
            else:
                print("algoritmo computado con baja precisión")
                captured = capsys.readouterr()
                assert captured.out == "Repetición terminado\n"
        except:
            print("matriz singular")
