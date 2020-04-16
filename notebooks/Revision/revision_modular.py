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
        - A (matriz): matriz cuadrada de dimensión nxn
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
        0.001711
    '''
    start_time=time.time()
    P,L,U=TodoJunto.PLU(A)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, P, L, U

def resuelve_bloques(A,B):
    '''
    Esta función ejecuta el algoritmo de SEL por medio de bloques y mide el tiempo de ejecución total del algoritmo. Se le debe 
    especificar una matriz cuadrada A y el vector B. La función devuelve el tiempo total en segundos de ejecución del 
    algoritmo, 2 matrices (L,U) y un vector P.
    
    * Para ver más información sobre la función solve_blocks, favor de consultar su documentación.

    ==========
    * Entradas:
        - A (matriz): matriz cuadrada de dimensión nxn
        - B(vector): vector de tamañano nx1
    * Salidas:
        - P (vector): nx1, con los índices de las columnas intercambiadas en el pivoteo.
        - L (matriz): matriz triangular inferior de nxn
        - U (matriz): matriz triangular superior nxn
        - timempo_total (float): tiempo total en segundos que tarda la ejecución del algoritmo PLU.
    ==========
    Ejemplo:
        >>A = np.array([[1.,  4., -2., -5.], [-3.,  9.,  8.,  7.], [5.,  1., -6., -4],[ 6., -1.,  2.,  8.]])
        >>B = np.array([3,0,7,6], dtype=np.float)
        >X 
        >array([ 0.99047619  0.52539683 -0.36269841  0.16349206])
    '''
    start_time=time.time()
    X_algoritmo=TodoJunto.solve_blocks(A,B)
    end_time=time.time()
    tiempo_total = end_time-start_time      
    return tiempo_total,X_algoritmo

def solve_A_b(A,b):
    '''
    Esta función ejecuta el algoritmo que resuelve un sistema de ecuaciones de la forma Ax = b con la
    factorización PLU y mide el tiempo de ejecución total del algoritmo. Se le debe especificar una matriz 
    cuadrada A y un vector de tamaño nx1. La función devuelve el tiempo total en segundos de ejecución del 
    algoritmo y un vector x de tamaño nx1 con la solución del sistema de ecuaciones.
    
    * Para ver más información sobre la función solve, favor de consultar su documentación.

    ==========
    * Entradas:
        - A (matriz): matriz cuadrada de dimensión nxn
        - b (vector): vector de nx1 con las soluciones del lado derecho del = de la ecuación 
    * Salidas:
        - x_est (vector): vector de nx1 con la solución del sistema de ecuaciones
    ==========
    Ejemplo:
        >>A = np.array([[2, 2, 3], [-4, -4, -3], [4, 8, 3]])
        >>b = np.array([1, 3, 2])
        >>solve_A_b(A)
        >x_est
        >array([-3.25,  1.25, 1.66])
        >tiempo_total
        0.000956
    '''
    start_time=time.time()
    x_est = TodoJunto.solve(A, b)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, x_est

def condicion(A):
    '''
    Esta función calcula la condición de la matriz cuadrada A. La condición sirve para ver cómo se comportará el algoritmo ante pequeñas perturbaciones en x.

    ==========
    * Entradas:
        - A: matriz cuadrada de dimensión nxn
    * Salidas:
        - cond (float): condicion de la matriz A
    ==========
    Ejemplo:
        >>A = np.array([[2, 2, 3], [-4, -4, -3], [4, 8, 3]])
        >>condicion(A)
        >cond
        13.882903
    '''
    cond=np.linalg.cond(A)
    return cond

def revision_PLU(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    '''
    El objetivo principal de esta función es revisar que la igualdad PA=LU se cumpla y generar un data 
    frame con información sobre la dimensión y condición de la matriz A, el tiempo de ejecución del 
    algoritmo PLU y el estado de la verificación de la igualdad (Ej: Correcto o Incorrecto).  
   
    Para cumplir con el objetivo principal, la función llama a otras funciones auxiliares: crea_matrices,
    condicion y factoriza_plu, que se describen arriba.  Se le debe especificar el número de veces que se 
    requiere quer se corra el algoritmo, el límite inferior y superior de la dimensión de la matriz y el 
    límite inferior y superior de los números de entrada a la matriz. La función devuelve un data frame 
    denominado resultados. 

    ==========
    * Entradas:
        - num_corridas (integer): número de veces que se requiere quer se corra el algoritmo
        - dim_limite_inf (integer): número entero que corresponde a la dimensión mínima de la matriz
        - dim_liminte_sup (integer): número entero que corresponde a la dimensión máxima de la matriz
        - entradas_lim_inf (integer): número entero que corresponde al número más chico que puede tener la 
        matriz como entrada
        - entradas_lim_sup (integer): número entero que corresponde al número más grande que puede tener
        la matriz como entrada
    * Salidas:
        - resultados (data frame): data frame con 4 columnas: dimension_A, condicion_A, tiemplo_plu y 
        status_plu
    ==========
    Ejemplo:
        >> num_corridas = 3
        >> dim_limite_inf = 2 
        >> dim_liminte_sup = 10^4 
        >> entradas_lim_inf = -99
        >> entradas_lim_sup = 99 
        >> revision_PLU(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        > resultados
        >|          | dimension_A | condicion_A | tiempo_plu | status_plu |
         |:--------:|:-----------:|:-----------:|------------|------------|
         |     0    |      37     |  104.049637 | 0.049255   | Correcto   |
         |     1    |      95     |  150.194068 | 0.434128   | Correcto   |
         |     2    |      34     |  48.884815  | 0.029457   | Correcto   |
    '''
    dimension_A=[]
    condicion_A=[]
    estado_plu=[]
    tiempo_plu=[]
    #tipo_matriz=[]
    for i in range(0,num_corridas):
        
        #modulo que crea matrices de forma aleatoria
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension_A.append(n)
        
        #modulo que calcula la condicion de A
        cond=condicion(A)
        condicion_A.append(cond)
        
        #modulo que implementa el algoritmo PLU y cuenta el tiempo
        tiempo_total, P, L, U=factoriza_plu(A)
        tiempo_plu.append(tiempo_total)
        
        if (np.allclose(np.dot(P, A), np.dot(L, U)))==True:
            status='Correcto'
            estado_plu.append(status)
            
        else:
            status='Incorrecto'
            estado_plu.append(status)
        
    data={'dimension_A':dimension_A,'condicion_A':condicion_A, 'tiempo_plu':tiempo_plu,'status_plu':estado_plu}       
    resultados=pd.DataFrame(data)
    return resultados
    
    
def revision_x(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    '''
    El objetivo principal de esta función es verificar que la solución estimada del sistema de ecuaciones 
    x_est sea la correcta al comparar con la x_real y generar un data frame con información sobre la 
    dimensión de la matriz A, el tiempo de ejecución del algoritmo solve que resuelve el sistema, el 
    estado de la verificación de la solución (Ej: Correcto o Incorrecto) y el error relativo entre x_est y 
    x_real. 
    
    Para cumplir con el objetivo principal, la función llama a otras funciones auxiliares: crea_matrices y 
    solve_A_b, que se describen arriba.  Se le debe especificar el número de veces que se 
    requiere quer se corra el algoritmo, el límite inferior y superior de la dimensión de la matriz y el 
    límite inferior y superior de los números de entrada a la matriz. La función devuelve un data frame 
    denominado resultados_x. 

    ==========
    * Entradas:
        - num_corridas (integer): número de veces que se requiere quer se corra el algoritmo
        - dim_limite_inf (integer): número entero que corresponde a la dimensión mínima de la matriz
        - dim_liminte_sup (integer): número entero que corresponde a la dimensión máxima de la matriz
        - entradas_lim_inf (integer): número entero que corresponde al número más chico que puede tener la 
        matriz como entrada
        - entradas_lim_sup (integer): número entero que corresponde al número más grande que puede tener
        la matriz como entrada
    * Salidas:
        - resultados_x (data frame): data frame con 4 columnas: dimension_A, condicion_A, tiempo_x, estado_x y error_x
    ==========
    Ejemplo:
        >> num_corridas = 3
        >> dim_limite_inf = 2 
        >> dim_liminte_sup = 10^4 
        >> entradas_lim_inf = -99
        >> entradas_lim_sup = 99 
        >> revision_x(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        > resultados_x
        >|          | dimension_A | condicion_A |  tiempo_x | estado_x |    error_x   |
         |:--------:|:-----------:|:-----------:|:---------:|----------|--------------|
         |     0    |      72     |  208.211964 |  0.212372 | Correcto | 1.579088e-14 |
         |     1    |      56     | 1247.565615 |  0.102223 | Correcto | 2.442450e-13 |
         |     2    |      32     | 2713.173540 |  0.025651 | Correcto | 5.905139e-13 |
    '''
    dimension_A=[]
    condicion_A=[]
    estado_x=[]
    tiempo_x=[]
    error_x=[]
    for i in range(0,num_corridas):
        
        #modulo que crea matrices de forma aleatoria
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension_A.append(n)
        
        #modulo que calcula la condicion de A
        cond=condicion(A)
        condicion_A.append(cond)

        x_real = np.round(np.random.normal(dim_limite_inf, dim_limite_sup, n),2)
        
        b = np.dot(A, x_real)
        tiempo_total_x,x_est = solve_A_b(A, b)
        tiempo_x.append(tiempo_total_x)
        status_x='Correcto' if np.allclose(x_est,x_real)==True else 'Incorrecto'
        estado_x.append(status_x)
        error_rel = np.mean(np.abs(x_real-x_est)/np.abs(x_real))
        error_x.append(error_rel)
         
    data={'dimension_A':dimension_A,'condicion_A':condicion_A,'tiempo_x':tiempo_x,'estado_x':estado_x,'error_x':error_x}       
    resultados_x=pd.DataFrame(data)
    return resultados_x

def revision_bloques(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    """
     Parametros
    ----------   
    num_corridas : numero de veces que queremos probar el algoritmo de "Solve_blocks"
    dim_limite_inf : es el límite inferior de las entradas para la matriz random a generar.
    dim_limite_sup : es el límite superior de las entradas para la matriz random a generar.
    entradas_lim_inf : es el límite inferior del tamaño de la matriz, buscamos matrices de nxn.
    entradas_lim_sup : es el límite superior del tamaño de la matriz, buscamos matrices de nxn.
        
    Salidas
    -------
    resultados : Un dataframe con el nombre de resultados, una vez evaluado el algoritmo con le número de corridas ingresadas.
    """
    dimension_A=[]
    condicion_A=[]
    solucion_bloques=[]
    tiempo_bloques=[]
    error_absoluto=[]
    
    for i in range(0,num_corridas):
        
        #modulo que crea la matriz random
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        X=np.random.randint(entradas_lim_inf,entradas_lim_sup,size=(n))
        B=A@X   
        dimension_A.append(n)
        
        #modulo que calcula la condicion de A
        cond=condicion(A)
        condicion_A.append(cond)
        
        tiempo_total,X_algoritmo=resuelve_bloques(A,B)
        tiempo_bloques.append(tiempo_total)
        
        error_abs=np.mean(np.fabs(X_algoritmo-X))
        error_absoluto.append(error_abs)
        
        if(np.allclose(X,X_algoritmo)==True):
            status='Correcto'
            solucion_bloques.append(status)
        else:
            pprint.pprint('Incorrecto para A igual a:')
            pprint.pprint(A)
            status='Incorrecto'
            solucion_bloques.append(status)

        
    data={'dimension_A':dimension_A, 'condicion_A':condicion_A,'tiempo_bloques':tiempo_bloques,'solucion_bloques':solucion_bloques,'error_abs':error_absoluto}       
    resultados_bloques=pd.DataFrame(data)
    return resultados_bloques

def revision_bloques_v2(num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    """
     Parametros
    ----------   
    num_corridas : numero de veces que queremos probar el algoritmo de "Solve_blocks"
    dim_limite_inf : es el límite inferior de las entradas para la matriz random a generar.
    dim_limite_sup : es el límite superior de las entradas para la matriz random a generar.
    entradas_lim_inf : es el límite inferior del tamaño de la matriz, buscamos matrices de nxn.
    entradas_lim_sup : es el límite superior del tamaño de la matriz, buscamos matrices de nxn.
        
    Salidas
    -------
    resultados : Un dataframe con el nombre de resultados, una vez evaluado el algoritmo con le número de corridas ingresadas.
    """
    dimension_A=[]
    condicion_A=[]
    solucion_bloques=[]
    tiempo_bloques=[]
    error_absoluto=[]
    
    for i in range(0,num_corridas):
        
        #modulo que crea la matriz random
        A,n=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        X=np.random.randint(entradas_lim_inf,entradas_lim_sup,size=(n))
        B=A@X   
        dimension_A.append(n)
        
        #modulo que calcula la condicion de A
        cond=condicion(A)
        condicion_A.append(cond)
        
        tiempo_total,X_algoritmo=resuelve_bloques(A,B)
        tiempo_bloques.append(tiempo_total)
        
        error_abs=np.mean(np.fabs(X_algoritmo-X))
        error_absoluto.append(error_abs)
        
        if(np.allclose(A@X_algoritmo,B)==True):
            status='Correcto'
            solucion_bloques.append(status)
        else:
            pprint.pprint('Incorrecto para A igual a:')
            pprint.pprint(A)
            status='Incorrecto'
            solucion_bloques.append(status)

        
    data={'dimension_A':dimension_A, 'condicion_A':condicion_A,'tiempo_bloques':tiempo_bloques,'solucion_bloques':solucion_bloques,'error_abs':error_absoluto}       
    resultados_bloques_v2=pd.DataFrame(data)
    return resultados_bloques_v2

