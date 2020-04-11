import numpy as np
import src.algorithms.eliminacionPorBloques as blocks
import src.algorithms.factorizacionPLU as plu


def prueba_bloques():
    eliminador = blocks.EliminacionPorBloques()
    B =  np.array([[ 1.,  4., -2., -5.,1],
               [-3.,  9.,  8.,  7.,2],
               [ 5.,  1., -6., -4.,3],
               [ 5.,  1., -6., -4.,4],
               [ 6., -1.,  2.,  8.,5]])

    A =  np.array([[ 1.,  4., -2., -5.],
               [-3.,  9.,  8.,  7.],
               [ 5.,  1., -6., -4.],
               [ 6., -1.,  2.,  8.]])

    b = np.array([3,0,7,6,9], dtype=np.float)
    a = np.array([3,0,7,6], dtype=np.float)

    x_prueba=np.linalg.solve(A,a)
    print(x_prueba)

    x_nuestra = eliminador.solve_blocks(A,a)
    print(x_nuestra)

    x_prueba=np.linalg.solve(B,b)
    print(x_prueba)

    x_nuestra = eliminador.solve_blocks(B,b)
    print(x_nuestra)
    
def prueba_lu():
    factorizador = plu.FactorizacionPLU()
    A = np.array([[2, 2, 3], 
              [-4, -4, -3], 
              [4, 8, 3]])
    b = np.array([-7, -1, 5])

    P, L, U = factorizador.PLU(A)

    np.matmul(P, A)
    np.matmul(L, U)

    print(np.linalg.solve(A, b))
    print(factorizador.solve(A, b))

def main():
    print("hello world!")
    prueba_bloques()
    prueba_lu()
    eliminador = blocks.EliminacionPorBloques()
    factorizador = plu.FactorizacionPLU()
    
    
    
    
if __name__ == "__main__":
    main()