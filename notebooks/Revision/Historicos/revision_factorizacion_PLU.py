import numpy as np
import scipy
import scipy.linalg
import pprint
import time
import pandas as pd
import factorizacion_PLU
import sys

def revision_PLU(nombre_archivo,numero_corridas,dimension_limite_inferior,dimension_limite_superior,entradas_limite_inferior,entradas_limite_superior):
    f= open(nombre_archivo,"w")
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    matrices_incorrectas=[]
    for i in range(0,numero_corridas):
        n=np.random.randint(dimension_limite_inferior, dimension_limite_superior)
        A=np.array(np.random.randint(entradas_limite_inferior,entradas_limite_superior, size=(n, n)))
        try:
            A_inv=np.linalg.inv(A)
        except:
            A_inv=None
        if (A_inv is not None and (np.allclose(np.dot(A, A_inv), np.eye(n))==True)):
            start_time=time.time()
            P,L,U=factorizacion_PLU.PLU(A)
            end_time=time.time()
            tiempo_total = end_time-start_time
        
            tiempo_plu.append(tiempo_total)
            dimension.append(n)
            
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
                
    data={'dimension':dimension,'status_plu':estado_plu, 'tiempo_plu':tiempo_plu,'matrices_incorrectas':matrices_incorrectas}       
    resultados=pd.DataFrame(data)
    return resultados
    f.close()
    
    
#resultados=revision_PLU('Resultados.txt',5,2,10,-99,99)
#resultados


#Karla 

#En esta parte ya solucioné lo del cálculo de la inversa y acorté el código para que no haga la comprobación de scipy y que eso se haga en otro lado. Este código crea la matriz, calcula PLU, verifica la singularidad y calcula los tiempos.

def revision_PLU(nombre_archivo,numero_corridas,dimension_limite_inferior,dimension_limite_superior,entradas_limite_inferior,entradas_limite_superior):
    f= open(nombre_archivo,"w")
    dimension=[]
    estado_plu=[]
    tiempo_plu=[]
    matrices_incorrectas=[]
    for i in range(0,numero_corridas):
        n=np.random.randint(dimension_limite_inferior, dimension_limite_superior)
        A=np.array(np.random.randint(entradas_limite_inferior,entradas_limite_superior, size=(n, n)))
        start_time=time.time()
        P,L,U=factorizacion_PLU.PLU(A)
        end_time=time.time()
        prod_diag = U.diagonal().prod()
        if prod_diag !=0:
            #print ("Matriz es no singular, continuar y comprobar valores de P,L y U")
            tiempo_total = end_time-start_time
            tiempo_plu.append(tiempo_total)
            dimension.append(n)
        else:
            print ("Matriz es singular y por lo tanto, el programa se va a detener")
            sys.exit()
    data={'dimension':dimension, 'tiempo_plu':tiempo_plu}       
    resultados=pd.DataFrame(data)
    return resultados
    f.close()
    
#resultados=revision_PLU('Resultados.txt',5,2,10,-99,99)
#resultados
