import numpy as np

def sodoku(matrix, n = 0):
    if n >= 81:
        return matrix
    
    if matrix.A1[n]:
        return sodoku(matrix, n + 1)

    i, j, k, l = n // 9, n % 9, n // 27 * 3, (n % 9) // 3 * 3

    x = set(range(1, 10)) - (
            set(matrix[i].A1) |
            set(matrix.T[j].A1) |
            set(matrix[k: k+3, l:l+3].A1)
            )

    #backtracking
    for value in x:
        matrix[i, j] = value
        if sodoku(matrix, n+1) is not None:
            return matrix
    else:
        matrix[i, j] = 0

print(sodoku(np.matrix(""" 8 0 0 1 0 9 0 7 0; 0 9 0 0 0 0 8 0 0; 5 0 3 0 4 0 0 0 0; 0 0 0 0 0 0 7 9 0; 0 0 7 2 6 5 3 0 0; 0 3 8 0 0 0 0 0 0; 0 0 0 0 9 0 4 0 1; 0 0 6 0 0 0 0 2 0; 0 5 0 4 0 2 0 0 3 """)))
