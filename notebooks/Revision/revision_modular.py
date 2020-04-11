import numpy as np
import pprint
import pandas as pd
import time
import factorizacion_PLU

def crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    n=np.random.randint(dim_limite_inf, dim_limite_sup)
    A=np.array(np.random.randint(entradas_lim_inf,entradas_lim_sup, size=(n, n)))
    x_real=np.array(np.random.randint(entradas_lim_inf,entradas_lim_sup, size=(n, 1)))
    return A,n,x_real

def factoriza_plu(A):
    start_time=time.time()
    P,L,U=factorizacion_PLU.PLU(A)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, P, L, U

def solve_A_b(A,b):
    start_time=time.time()
    x_est = factorizacion_PLU.solve(A, b)
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
        A,n,x_real=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
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
    for i in range(0,num_corridas):
        #modulo que crea matrices de forma aleatoria
        A,n,x_real=crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)
        
        b = np.dot(A, x_real)
        tiempo_total_x,x_est = solve_A_b(A, b)
        tiempo_x.append(tiempo_total_x)
        status_x='Correcto' if np.allclose(x_est,x_real)==True else 'Incorrecto'
        estado_x.append(status_x)
        
        
    data={'dimension':dimension,'tiempo_x':tiempo_x,'estado_x':estado_x}       
    resultados=pd.DataFrame(data)
    return resultados
    
    