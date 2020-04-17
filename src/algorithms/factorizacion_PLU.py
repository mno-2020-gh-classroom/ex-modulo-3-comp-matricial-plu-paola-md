import numpy as np
from scipy.linalg import solve_triangular

to_n = lambda n: np.arange(1, n+1)
indexr = lambda i: i-1

def forward_substitution(L, b):
    to_n = lambda n: np.arange(1, n+1)
    indexr = lambda i: i-1
    '''
    Algoritmo de Forward substitution orientado a FILAS

    Esta función devuelve b para un sistema:
    Lx = b (1)
    ==========
    * Entradas:
        - L (array): matriz no singular, triangular inferior de nxn.
        - b (array): vector de nx1
    * Salidas:
        - y (array): vector de nx1, solución del sistema (1): Lx = b
    ==========
    Ejemplo:
        >>L = np.matrix([[1,0],[2,3]])
        >>b = np.array([2, 22])
        >>forward_substitution(L,b)
        > [2.0, 6.0]

    ==========
    Ref.:
    GCV - matrix computations (2013)
    Row-Oriented Forward Substitution (algorithm 3.1.1), p.106
    *********************
    Notas:
    Falta poner warnings por si el usuario mete inputs malos:
        ej: matriz no ciuadrada, matriz singular, las dimensiones de b
        y Y no coinciden
    '''
    n = len(b)
    y = np.zeros(n)
    y[indexr(1)] = b[indexr(1)]/L[indexr(1), indexr(1)]
    for i in np.arange(2, n+1):
        suma = 0
        for j in to_n(i-1):
            suma = suma + L[indexr(i), indexr(j)]*y[indexr(j)]
        y[indexr(i)] = (b[indexr(i)] - suma)/L[indexr(i), indexr(i)]

    return(y)

def backward_substitution(U, b):
    to_n = lambda n: np.arange(1, n+1)
    indexr = lambda i: i-1
    '''
    Algoritmo de Backward substitution orientado a FILAS

    Esta función devuelve b para un sistema:
    Lx = b (1)
    ==========
    * Entradas:
        - U (array): matriz no singular, triangular superior de nxn.
        - b (array): vector de nx1
    * Salidas:
        - y: vector de nx1, solución del sistema (1): Ux = b
    ==========
    Ejemplo:
        >>U = np.matrix([[1, 2],[0,3]])
        >>b = np.array([49, 21])
        >>BackwardSubsRow(U,b)
        > array([35.,  7.])

    ==========
    Ref.:
    GCV - matrix computations (2013)
    Row-Oriented Backward Substitution (algorithm 3.1.2), p.107
    '''
    n = len(b)
    x = np.zeros(n)
    x[indexr(n)] = b[indexr(n)]/U[indexr(n), indexr(n)]
    for i in np.arange(1, n-1+1)[::-1]:
        suma = 0
        for j in np.arange(i+1, n+1):
            suma = suma + U[indexr(i), indexr(j)]*x[indexr(j)]
        x[indexr(i)] = (b[indexr(i)] - suma)/U[indexr(i), indexr(i)]

    return(x)

def get_P(piv):
    to_n = lambda n: np.arange(1, n+1)
    indexr = lambda i: i-1
    '''
    Esta función obtiene la matriz pivote derivada del intercambio de elementos
    en la matriz identidad original
    ==========
    * Entradas:
        - p: índices
    * Salidas:
        - P (matriz): matriz de permutación de nxn

    '''
    n = len(piv) + 1
    P = np.eye(n)
    for j in to_n(n-1):
        aux = P[indexr(j), :].copy()
        P[indexr(j), :] = P[indexr(piv[indexr(j)]), :].copy()
        P[indexr(piv[indexr(j)]), :] = aux.copy()

    return(P)

def PLU_test(A):
    '''
    Esta función desarrolla la factorizacióón PA = LU, donde P es la matriz de
    permutación codificada por piv(l:n - 1), guarda los ííndices fila de los
    pivotes, de tal modo que la columnas intercambiadas se guardan en el vector
    P.
    Esta función devuelve P en el sistema:
    Lx = b (1)
    ==========
    * Entradas:
        - A: array de nxn.
    * Salidas:
        - P (vector): nx1, con los ííndices de las columnas intercambiadas en
        el pivoteo.
        - L (matriz): matriz triangular inferior de nxn
        - U (matriz): matriz triangular superior nxn
    ==========
    Ejemplo:
        >>A = np.array([[2, 2, 3], [-4, -4, -3], [4, 8, 3]])
        >>P, L, U = PLU(A)
        >>P
        >array([[0., 1., 0.],
       [0., 0., 1.],
       [1., 0., 0.]])
        >>L
        >array([[ 1. ,  0. ,  0. ],
       [-1. ,  1. ,  0. ],
       [-0.5,  0. ,  1. ]])
        >>U
        >array([[-4. , -4. , -3. ],
       [ 0. ,  4. ,  0. ],
       [ 0. ,  0. ,  1.5]])
       >>np.matmul(P, A)==np.matmul(L, U)
       >array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]])
    '''
    to_n = lambda n: np.arange(1, n+1)
    indexr = lambda i: i-1
    # inicialización de elementos
    A = A.astype('float64')
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    piv = np.arange(1, n-1+1)
    v = np.zeros(n)

    for j in to_n(n):
        if j == 1:
            v = A[indexr(j):n, indexr(j)].copy()
        else:
            a = A[:, indexr(j)].copy()
            for k in to_n(j-1):
                aux = a[indexr(k)].copy()
                a[indexr(k)] = a[indexr(piv[indexr(k)])].copy()
                a[indexr(piv[indexr(k)])] = aux.copy()
            z = forward_substitution(L[indexr(1):(j-1), indexr(1):(j-1)], a[indexr(1):(j-1)])
            U[indexr(1):(j-1), indexr(j)] = z.copy()
            v[indexr(j):n] = (a[indexr(j):n]-np.matmul(L[indexr(j):n, indexr(1):(j-1)], z)).copy()

        if j < n:
            mu = (np.argmax(np.abs(v[indexr(j):n]))+j).copy()
            piv[indexr(j)] = mu.copy()
            aux = v[indexr(j)].copy()
            v[indexr(j)] = v[indexr(mu)].copy()
            v[indexr(mu)] = aux.copy()
            if v[indexr(j)] != 0:
                L[indexr(j+1):n, indexr(j)] = (v[indexr(j+1):n]/v[indexr(j)]).copy()
            if j > 1:
                aux = L[indexr(j), indexr(1):(j-1)].copy()
                L[indexr(j), indexr(1):(j-1)] = L[indexr(mu), indexr(1):(j-1)].copy()
                L[indexr(mu), indexr(1):(j-1)] = aux.copy()
        U[indexr(j), indexr(j)] = v[indexr(j)].copy()

    P = get_P(piv)

    return P, L, U

def simulate(n, times):
    error_abs = np.zeros(times)
    for i in to_n(times):
        np.random.seed(i)
        A = np.random.normal(0, 1, (n, n))
        x_real = np.random.normal(0, 1, n)
        b = np.matmul(A, x_real)
        x_est = solve(A, b)
        error_abs[indexr(i)] = np.sum(np.abs(x_real-x_est))

    return(np.mean(error_abs))
