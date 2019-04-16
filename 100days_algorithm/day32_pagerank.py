import networkx as nx
import numpy as np

def pagerank(graph, alpha=.9):
    n = len(graph)

    # remove links to self
    graph[range(n), range(n)] = 0

    # ensure stochasticity
    graph[:, graph.sum(0) == 0] = 1
    graph /= graph.sum(0)

    # add random teleports
    graph = alpha * graph + (1 - alpha) / n * np.ones((n,n))

    # power iteration
    prev = np.zeros(n)
    rank = prev + 1/n
    while (rank - prev) @ (rank - prev) > 1e-8:
        prev = rank
        rank = graph @ rank

    return rank

n = 10
graph = nx.DiGraph()
graph.add_nodes_from(range(n))
graph.add_edges_from(np.random.randint(0, n, (3*n, 2)))

pagerank(
        np.array(nx.adjacency_matrix(graph).todense(), dtype=np.float32)
        ).round(2)
