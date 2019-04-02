import numpy as np

def mult(x, y):
    nx, ny = len(x), len(y)

    #auxiliary x
    fx = np.zeros(nx + ny, np.float64)
    fx[:nx] = list(map(int, reversed(x)))

    #auxiliary y
    fy = np.zeros(nx + ny, np.float64)
    fy[:ny] += list(map(int, reversed(y)))

    # convolution via FFT
    fx = np.fft.fft(fx)
    fy = np.fft.fft(fy)
    z = np.fft.ifft(fx*fy).real.round().astype(int)

    #carry over
    for i in range(nx + ny - 1):
        z[i+1] += z[i] // 10
        z[i] %= 10

    return ''.join(map(str, reversed(z)))

print(mult('987432', '23487'))


