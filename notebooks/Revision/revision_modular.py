import numpy as np
import pprint
import scipy  
import scipy.linalg
import pandas as pd
import factorizacion_PLU
import crea_matrices
import factoriza_plu

def revision_PLU(nombre_archivo,num_corridas,dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    f= open(nombre_archivo,"w")
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    matrices_incorrectas=[]
    for i in range(0,num_corridas):
        
        #modulo que crea la matriz random
        A,n=crea_matrices.crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup)
        dimension.append(n)
        
        #modulo de conteo de tiempo
        tiempo_total, P, L, U=factoriza_plu.factoriza_plu(A)
        tiempo_plu.append(tiempo_total)
        
        P_correcta, L_correcta, U_correcta = scipy.linalg.lu(A)
        
        if (np.allclose(P, P_correcta)==True and np.allclose(L, L_correcta)==True and np.allclose(U, U_correcta)==True):
            status='Correcto'
            estado_plu.append(status)
            matrices_incorrectas.append('')
        else:
            if ((np.allclose(P, P_correcta)==False) and (np.allclose(L, L_correcta)==False) and (np.allclose(U, U_correcta)==False)):
                matrices_incorrectas.append('P-L-U')
            elif ((np.allclose(P, P_correcta)==False) and (np.allclose(L, L_correcta)==False)):
                matrices_incorrectas.append('P-L')
            elif ((np.allclose(P, P_correcta)==False) and (np.allclose(U, U_correcta)==False)):
                matrices_incorrectas.append('P-U')
            elif ((np.allclose(L, L_correcta)==False) and (np.allclose(U, U_correcta)==False)):
                matrices_incorrectas.append('L-U')
            elif np.allclose(P, P_correcta)==False:
                matrices_incorrectas.append('P')
            elif np.allclose(L, L_correcta)==False:
                matrices_incorrectas.append('L')
            elif np.allclose(U, U_correcta)==False:
                matrices_incorrectas.append('U')
                          
            status='Incorrecto'
            estado_plu.append(status)
        
            pprint.pprint('Incorrecto para A igual a:',f)
            pprint.pprint(A, f)
            pprint.pprint('P algoritmo:',f)
            pprint.pprint(P, f)
            pprint.pprint('P correcta:',f)
            pprint.pprint(P_correcta, f)
            pprint.pprint('L algoritmo',f)
            pprint.pprint(L, f)
            pprint.pprint('L correcta',f)
            pprint.pprint(L_correcta, f)
            pprint.pprint('U algoritmo:',f)                
            pprint.pprint(U, f)
            pprint.pprint('U correcta:',f)
            pprint.pprint(U_correcta, f)
        
    data={'dimension':dimension, 'tiempo_plu':tiempo_plu,'status_plu':estado_plu,'matrices_incorrectas':matrices_incorrectas}       
    resultados=pd.DataFrame(data)
    return resultados
    f.close()
    
  