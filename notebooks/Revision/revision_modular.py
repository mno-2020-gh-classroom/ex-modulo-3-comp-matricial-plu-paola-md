import numpy as np
import pprint
import pandas as pd
import time
import TodoJunto

def crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    '''
    Esta función crea matrices de forma aleatoria. Se le debe especificar el límite inferior y        
    superior de la dimensión de la matriz y el límite inferior y superior de los números de entrada a 
    la matriz. La función devuelve una matriz A cuadrada de dimensión nxn:

    ==========
    * Entradas:
        - dim_limite_inf (integer): número entero que corresponde a la dimensión mínima de la matriz
        - dim_liminte_sup (integer): número entero que corresponde a la dimensión máxima de la matriz
        - entradas_lim_inf (integer): número entero que corresponde al número más chico que puede tener la 
        matriz como entrada
        - entradas_lim_sup (integer): número entero que corresponde al número más grande que puede tener
        la matriz como entrada
    * Salidas:
        - A (matriz): matriz cuadrada de dimensión nxn
    ==========
    Ejemplo:
        >> dim_limite_inf = 2 
        >> dim_liminte_sup = 10^4 
        >> entradas_lim_inf = -99
        >> entradas_lim_sup = 99 
        >> crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        > A
        >array([[-28, -50,  79],
                 [-22,  87, -23],
                 [  0, -97,  22]])
    '''
    n=np.random.randint(dim_limite_inf, dim_limite_sup)
    A=np.array(np.random.randint(entradas_lim_inf,entradas_lim_sup, size=(n, n)))
    return A,n

def factoriza_plu(A):
    '''
    Esta función ejecuta el algoritmo de PLU y mide el tiempo de ejecución total del algoritmo. Se le debe 
    especificar una matriz cuadrada A. La función devuelve el tiempo total en segundos de ejecución del 
    algoritmo, 2 matrices (L,U) y un vector P.
    
    * Para ver más información sobre la función factorización_PLU, favor de consultar su documentación.

    ==========
    * Entradas:
        - A: matriz cuadrada de dimensión nxn
    * Salidas:
        - P (vector): nx1, con los índices de las columnas intercambiadas en el pivoteo.
        - L (matriz): matriz triangular inferior de nxn
        - U (matriz): matriz triangular superior nxn
        - timempo_total (float): tiempo total en segundos que tarda la ejecución del algoritmo PLU.
    ==========
    Ejemplo:
        >>A = np.array([[2, 2, 3], [-4, -4, -3], [4, 8, 3]])
        >>factoriza_plu(A)
        >P
        >array([[0., 1., 0.],
               [0., 0., 1.],
               [1., 0., 0.]])
        >L
        >array([[ 1. ,  0. ,  0. ],
               [-1. ,  1. ,  0. ],
               [-0.5,  0. ,  1. ]])
        >U
        >array([[-4. , -4. , -3. ],
               [ 0. ,  4. ,  0. ],
               [ 0. ,  0. ,  1.5]])
        >tiempo_total
        0.51068
    '''
    start_time=time.time()
    P,L,U=TodoJunto.PLU(A)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, P, L, U

def solve_A_b(A,b):
    start_time=time.time()
    x_est = TodoJunto.solve(A, b)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, x_est

def revision_PLU(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    #tipo_matriz=[]
    for i in range(0,num_corridas):
        
        #modulo que crea matrices de forma aleatoria
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)
        
        #modulo que implementa el algoritmo PLU y cuenta el tiempo
        tiempo_total, P, L, U=factoriza_plu(A)
        tiempo_plu.append(tiempo_total)
        
        
        if (np.allclose(np.dot(P, A), np.dot(L, U)))==True:
            status='Correcto'
            estado_plu.append(status)
            
            
        else:
            status='Incorrecto'
            estado_plu.append(status)
            
                    
        
    data={'dimension':dimension, 'tiempo_plu':tiempo_plu,'status_plu':estado_plu}       
    resultados=pd.DataFrame(data)
    return resultados
    
    
def revision_x(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    dimension=[]
    estado_x=[]
    tiempo_x=[]
    error_x=[]
    for i in range(0,num_corridas):
        #modulo que crea matrices de forma aleatoria
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)

        x_real = np.round(np.random.normal(dim_limite_inf, dim_limite_sup, n),2)
        
        b = np.dot(A, x_real)
        tiempo_total_x,x_est = solve_A_b(A, b)
        tiempo_x.append(tiempo_total_x)
        status_x='Correcto' if np.allclose(x_est,x_real)==True else 'Incorrecto'
        estado_x.append(status_x)
        error_rel = np.mean(np.abs(x_real-x_est)/np.abs(x_real))
        error_x.append(error_rel)
        
        
    data={'dimension':dimension,'tiempo_x':tiempo_x,'estado_x':estado_x,'error_x':error_x}       
    resultados=pd.DataFrame(data)
    return resultados
    
    