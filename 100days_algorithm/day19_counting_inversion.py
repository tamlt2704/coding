def inversions(items):
    n = len(items)
    if n <= 1:
        return items, 0

    left, linv = inversions(items[:n // 2])
    right, rinv = inversions(items[n // 2:])

    inv = linv + rinv
    llen, rlen = len(left), len(right)
    i, j, aux = 0, 0, []

    for k in range(n):
        if i < llen and j < rlen and left[i] > right[j]:
            inv += llen -i
            aux.append(right[j])
            j+=1
        elif i < llen:
            aux.append(left[i])
            i+=1
        else:
            aux.append(right[j])
            j+=1
    return aux, inv
print(inversions([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))
