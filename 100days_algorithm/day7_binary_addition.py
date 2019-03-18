from itertools import zip_longest
import ipdb

p0c0 = 0, {}
p1c0 = 1, {}
p0c1 = 0, {}
p1c1 = 1, {}

p0c0[1].update({(0,0): p0c0, (1,0): p1c0, (0,1): p1c0, (1,1): p0c1})
p1c0[1].update({(0,0): p0c0, (1,0): p1c0, (0,1): p1c0, (1,1): p0c1})
p0c1[1].update({(0,0): p1c0, (1,0): p0c1, (0,1): p0c1, (1,1): p1c1})
p1c1[1].update({(0,0): p1c0, (1,0): p0c1, (0,1): p0c1, (1,1): p1c1})


def add(x, y):
    x = map(int, reversed(x))
    y = map(int, reversed(y))
    z = []

    value, transition = p0c0
    for r, s in zip_longest(x, y, fillvalue=0):
        ipdb.set_trace()
        value, transition = transition[r,s]
        z.append(transition[0,0][0])

    # handle carry
    z.append(transition[0,0][0])


    return ''.join(map(str, reversed(z)))

print(add('1100100100100', '100100011000'))




