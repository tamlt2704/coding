import numpy as np
import matplotlib.pyplot as plt

def kmeans(points, n_clusters):

    sample = np.random.choice(len(points), n_clusters, replace=False)
    centroid = points[sample]

    loss = [-1, -2]
    while not np.allclose(*loss):
        distance = [np.sqrt(((points -c) ** 2).sum(1)) for c in centroid]

        loss = loss[1:] + [np.sum(distance)]
        cluster = np.argmin(distance, axis=0)

        for i in range(n_clusters):
            centroid[i] = np.mean(points[cluster == i], axis=0)

    return cluster

n = 100
A = np.random.multivariate_normal([2, 0], [[1, .1], [-4, 1]], n)
B = np.random.multivariate_normal([-2, 0], [[1, -4], [.1, 1]], n)
C = np.random.multivariate_normal([2, -2], [[1, 4], [-.1, 1]], n)
D = ['red', 'green', 'blue']

points = np.r_[A, B, C]
original_color = np.repeat(D[:3], n)

cluster = kmeans(points, 3)
