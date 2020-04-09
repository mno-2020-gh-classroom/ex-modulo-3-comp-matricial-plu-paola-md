import numpy as np
from scipy.linalg import solve_triangular

to_n = lambda n: np.arange(1, n+1)
indexr = lambda i: i-1

#Factorización PLU

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    y[indexr(1)] = b[indexr(1)]/L[indexr(1), indexr(1)]
    for i in np.arange(2, n+1):
        suma = 0
        for j in to_n(i-1):
            suma = suma + L[indexr(i), indexr(j)]*y[indexr(j)]
        y[indexr(i)] = (b[indexr(i)] - suma)/L[indexr(i), indexr(i)]
    
    return(y)
    
def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    x[indexr(n)] = y[indexr(n)]/U[indexr(n), indexr(n)]
    for i in np.arange(1, n-1+1)[::-1]:
        suma = 0
        for j in np.arange(i+1, n+1):
            suma = suma + U[indexr(i), indexr(j)]*x[indexr(j)]
        x[indexr(i)] = (y[indexr(i)] - suma)/U[indexr(i), indexr(i)]
    
    return(x)

def get_P(piv):
    n = len(piv) + 1
    P = np.eye(n)
    for j in to_n(n-1):
        aux = P[indexr(j), :].copy()
        P[indexr(j), :] = P[indexr(piv[indexr(j)]), :].copy()
        P[indexr(piv[indexr(j)]), :] = aux.copy()
        
    return(P)

def PLU(A):
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
            #z = solve_triangular(L[indexr(1):(j-1), indexr(1):(j-1)], a[indexr(1):(j-1)], lower = True).copy()
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
    return({'L':L, 'U':U, 'piv':piv, 'P':P})
    
A = np.array([[0, 0, 4], 
              [1, 3, 2], 
              [2, 8, 4]])

PLU(A)['piv']
PLU(A)['L']
PLU(A)['U']
PLU(A)['P']

P = PLU(A)['P']
L = PLU(A)['L']
U = PLU(A)['U']

np.matmul(P, A)
np.matmul(L, U)

#Resolver sistema de ecuaciones Ax = b

def solve(A, b):
    A = A.astype('float64')
    b = b.astype('float64')
#Paso 1

    fact = PLU(A)
    P = fact['P']
    L = fact['L']
    U = fact['U']

#Paso 2
    
    #d = solve_triangular(L, np.matmul(P, b), lower = False)
    d = forward_substitution(L, np.matmul(P, b))
    
#Paso 3
    
    #x = solve_triangular(U, d, lower = True)
    x = backward_substitution(U, d)
    
    return(x)

A = np.array([[2, 1, -1], 
              [1, -2, 2], 
              [3, -2, 1]])
b = np.array([1, 3, 2])

fact = PLU(A)
P = fact['P']
L = fact['L']
U = fact['U']

np.matmul(P, A)
np.matmul(L, U)

np.linalg.solve(A, b)
solve(A, b)

A = np.array([[2, 2, 3], 
              [-4, -4, -3], 
              [4, 8, 3]])
b = np.array([-7, -1, 5])

fact = PLU(A)
P = fact['P']
L = fact['L']
U = fact['U']

np.matmul(P, A)
np.matmul(L, U)

np.linalg.solve(A, b)
solve(A, b)

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

n = 10^4
times = 100
simulate(n, times)

