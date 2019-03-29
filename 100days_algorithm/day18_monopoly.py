def probability(n):
    p = [0, 0, 0, 0, 0, 1]

    for _ in range(n):
        p.append(sum(p[-6:]) / 6)

    return p[6:]
