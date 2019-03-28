import numpy as np

X = np.array([
    [0, 1, 1], [1, 0, 1], [1, 1, 1], [-1, 1, 1], [1, -1, 1]
    ])
Y = np.array([1,1,1, 0, 0])
W = np.zeros(3)

def perceptron(x, w):
    return (x @ w >=0).astype(int)

def train(x, y, w):
    for i in range(len(x)):
        h = perceptron(x[i,:], w)

        if h != y[i]:
            if y[i] == 1:
                w += x[i, :]
            else:
                w -= x[i, :]
    return perceptron(x, w)

for _ in range(5):
    h = train(X, Y, W)
    print('w=', W, 'acc=', np.mean(h==Y))

