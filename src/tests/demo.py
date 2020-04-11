import numpy as np
import src.algorithms.EliminacionPorBloques as blocks
import src.algorithms.FactorizacionPLU as plu


def prueba_bloques():
    eliminador = blocks.EliminacionPorBloques()
    MAT_B =  np.array([[ 1.,  4., -2., -5.,1],
               [-3.,  9.,  8.,  7.,2],
               [ 5.,  1., -6., -4.,3],
               [ 5.,  1., -6., -4.,4],
               [ 6., -1.,  2.,  8.,5]])

    MAT_A =  np.array([[ 1.,  4., -2., -5.],
                       [-3.,  9.,  8.,  7.],
                       [ 5.,  1., -6., -4.],
                       [ 6., -1.,  2.,  8.]])

    sol_b = np.array([3,0,7,6,9], dtype=np.float)
    sol_a = np.array([3,0,7,6], dtype=np.float)

    x_prueba=np.linalg.solve(MAT_A,sol_a)
    print(x_prueba)

    x_nuestra = eliminador.solve_blocks(MAT_A,sol_a)
    print(x_nuestra)

    x_prueba=np.linalg.solve(MAT_B,sol_b)
    print(x_prueba)

    x_nuestra = eliminador.solve_blocks(MAT_B,sol_b)
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
    
    MAT_A =  np.array([[ 1.,  4., -2., -5.],
                       [-3.,  9.,  8.,  7.],
                       [ 5.,  1., -6., -4.],
                       [ 6., -1.,  2.,  8.]])
    
    sol_a = np.array([3,0,7,6], dtype=np.float)
    
    print(np.linalg.solve(MAT_A, sol_a))
    print(factorizador.solve(MAT_A, sol_a))
    
    
        
    MAT_A =  np.array([[ 0.,  0., 0., -5.],
                       [-3.,  9.,  0.,  7.],
                       [ 5.,  1.,  0., -4.],
                       [ 6., -1.,  0.,  8.]])
    
    sol_a = np.array([3,0,7,6], dtype=np.float)
    
    #print(np.linalg.solve(MAT_A, sol_a))
    print(factorizador.solve(MAT_A, sol_a))

def main():
    print("Vamos a probaaar :)")
    prueba_bloques()
    #prueba_lu()
    
    
    
    
if __name__ == "__main__":
    main()