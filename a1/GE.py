import numpy as np

A = np.array([[1, 0, 1, 1],
              [1, 0, 1, 1],
              [0, 1, 1, 1],
              [1, 1, 1, 0],
              [1, 1, 1, 0]], dtype=np.float64)

P_row = 0 #/* Initialization of the pivot row */
P_col = 0 #/* Initialization of the pivot column */

m = 5
n = 4

def swap_rows(P_row, r_max):
    return P_row + r_max

while P_row <= m and P_col <= n:
    #Find the k-th pivot: argmax (i = P_row ... m, abs(A[i][col]))
    r_max = list(A[P_row : m + 1, P_col]).index(max(A[P_row : m + 1, P_col]))
    if A[r_max][P_col] == 0:
        P_col = P_col + 1
    else:
        # swap_rows(P_row, r_max)
        A[[P_row, r_max], :] = A[[r_max, P_row], :]
        #Do for all rows below pivot:
        for r in range(P_row + 1, m + 1):
            f = A[r][P_col] / A[P_row][P_col]
            #Fill with zeros the lower part of pivot column:
            A[r][P_col] = 0
            #Do for all remaining elements in current row:
            for c in range(P_col + 1, n + 1):
                A[r][c] = A[r][c] - A[P_row][c] * f
        #Increase pivot row and column 
        P_row = P_row + 1
        P_col = P_col + 1
         # for r in range(P_row + 1, m):
        #     f           = X[r][P_col] / X[P_row][P_col]
        #     X[r][P_col] = 0 # Fill with zeros the lower part of pivot column:
        #     # Do for all remaining elements in current row:
        #     for c in range(P_col + 1, n):
        #         X[r][c] = X[r][c] - X[P_row][c] * f
