import numpy as np

def determinant(x):
    if x.size == 1:
        return x[0, 0]

    # pivot
    i = np.abs(x[:, 0]).argmax()
    pivot = x[i, 0]
    
    if np.abs(pivot) < 1e-15:
        return 0

    # gauss elimination
    n = len(x)
    y = x - x[:, 0].reshape(n,1) @ \
            (x[i, :] / x[i, 0]).reshape(1, n)
    y = y[np.arange(n) != i, 1:]

    #recursion
    return pivot * (-1) ** (i % 2) * determinant(y)

X = np.array([[4,9,2], [3, 5, 7], [8, 1, 6]])
print(determinant(X))
