import numpy as np
import scipy 
from math import ceil
from src.algorithms.FactorizacionPLU import solve

class EliminacionPorBloques():
    
    #Cambiar en el futuro
    def nuestro_algoritmo(self, A, b):
        return np.linalg.solve(A,b)

    def solve_blocks(self,A,b):    
        # Check that it is a squared matrix
        A_column = A.shape[1]
        if A_column == A.shape[0]:
            if A_column % 2 == 0:
                x  = int(A_column/2)
            else:
                x = int(ceil(A_column/2))

            A11 = A[:x,:x]
            A12 = A[:x,x:]
            A21 = A[x:,:x]
            A22 = A[x:,x:]

            b1 = b[:x]
            b2 = b[x:]

            A11_b1 = self.nuestro_algoritmo(A11, b1)
            A11_A12 = self.nuestro_algoritmo(A11, A12)

            Schur = A22 - A21@A11_A12
            b_hat = b2 - A21@A11_b1

            x2 = self.nuestro_algoritmo(Schur, b_hat)
            x1 = self.nuestro_algoritmo(A11, (b1-A12@x2))

            X = np.block([x1,x2])
        else:
            X = 0
            print("Please enter a squared matrix")
        return X




