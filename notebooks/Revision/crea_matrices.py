import numpy as np

def crea_matrices(dim_limite_inf,dim_limite_sup,entradas_lim_inf,entradas_lim_sup):
    n=np.random.randint(dim_limite_inf, dim_limite_sup)
    A=np.array(np.random.randint(entradas_lim_inf,entradas_lim_sup, size=(n, n)))
    return A,n

    