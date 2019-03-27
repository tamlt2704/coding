def swap(x, y):
    s = x < y
    return x * s + y * (1-s), y*s + x*(1-s)

print(swap(3, 15))
print(swap(15, 3))
