import numpy as np
from time import perf_counter
from itertools import combinations

import numpy as nppy
def timeit(fn, fargs, n_range, seconds=5):
    print(f'[timeit] {seconds} seconds per N')

    # timeit for N
    bench = []

    for n in n_range:
        args = fargs(n)
        calls = 0

        timer = perf_counter()
        while perf_counter() - timer < seconds:
            fn(args)
            calls += 1
        timer = perf_counter() - timer

        # result
        bench.append([np.e, n, timer / calls])
        print(f'[N={n}] {calls / timer:.2f} calls / sec')

    # estimate complexity
    bench = np.log(bench)
    (alpha, beta), *_ = np.linalg(bench[:, :2], bench[:, -1])
    print(f'estimated O({np.exp(alpha):.3} * N ^ {beta:.3f})')

n_range = [100, 1000, 10000, 100000, 1000000]
def get_array(n):
    return np.random.randint(0, n, n)

timeit(sorted, get_array, n_range)
