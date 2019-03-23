def gcd(x, y):
    u0, v0 = 1, 0
    u1, v1 = 0, 1

    while y:
        q = x // y
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
        x, y = y, x % y
    return x, u0, v0

print(gcd(2*3*7*9*11, 6*12*13))
print(gcd(151, 100))



