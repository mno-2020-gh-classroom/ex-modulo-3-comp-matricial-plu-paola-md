import numpy as np
import pprint
import pandas as pd
#import factorizacion_PLU

def crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    n=np.random.randint(dim_limite_inf, dim_limite_sup)
    A=np.array(np.random.randint(entradas_lim_inf,entradas_lim_sup, size=(n, n)))
    return A,n

def factoriza_plu(A):
    start_time=time.time()
    P,L,U=factorizacion_PLU.PLU(A)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, P, L, U

def revision_PLU(nombre_archivo,num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    f= open(nombre_archivo,"w")
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    #tipo_matriz=[]
    for i in range(0,num_corridas):
        
        #modulo que crea matrices de forma aleatoria
        A,n=crea_matrices.crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)
        
        #modulo que implementa el algoritmo PLU y cuenta el tiempo
        tiempo_total, P, L, U=factoriza_plu.factoriza_plu(A)
        tiempo_plu.append(tiempo_total)
        
        
        if (np.allclose(np.dot(P, A), np.dot(L, U)))==True:
            status='Correcto'
            estado_plu.append(status)
            
        else:
            status='Incorrecto'
            estado_plu.append(status)
        
            pprint.pprint('Incorrecto para A igual a:',f)
            pprint.pprint(A, f)
            pprint.pprint('P:',f)
            pprint.pprint(P, f)
            pprint.pprint('L',f)
            pprint.pprint(L, f)
            pprint.pprint('U:',f)                
            pprint.pprint(U, f)

        
    data={'dimension':dimension, 'tiempo_plu':tiempo_plu,'status_plu':estado_plu}       
    resultados=pd.DataFrame(data)
    return resultados
    f.close()
    
  