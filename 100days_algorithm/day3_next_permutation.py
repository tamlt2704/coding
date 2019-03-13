import sys 


def next_permutation(x):
    n = len(x)
    for i in reversed(range(n-1)):
        if x[i] < x[i+1]:
            break
    else:
        return x[::-1]



    for j in reversed(range(i, n)):
        if x[i] < x[j]:
            x[i],x[j] = x[j],x[i]
            x[i+1:] = x[i+1:][::-1]
    return x


x = list('FADE') if len(sys.argv) < 2 else list(sys.argv[1])
print (x)
print("=>", next_permutation(x))

