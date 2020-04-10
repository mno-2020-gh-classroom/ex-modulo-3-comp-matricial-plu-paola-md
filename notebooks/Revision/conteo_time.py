import time
import factorizacion_PLU

def conteo_time(A):
    start_time=time.time()
    P,L,U=factorizacion_PLU.PLU(A)
    end_time=time.time()
    tiempo_total = end_time-start_time
    return tiempo_total, P, L, U