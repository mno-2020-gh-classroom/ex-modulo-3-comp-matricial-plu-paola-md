import numpy as np
import pprint
import pandas as pd
#import factorizacion_PLU
import crea_matrices
import factoriza_plu

def revision_PLU(nombre_archivo,num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    f= open(nombre_archivo,"w")
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    #tipo_matriz=[]
    for i in range(0,num_corridas):
        
        #modulo que crea la matriz random
        A,n=crea_matrices.crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)
        
        #modulo de conteo de tiempo
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
    
  