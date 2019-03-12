

def mult(chain):
    n = len(chain)

    # init
    aux = {(i,i): (0,) + chain[i] for i in range(n)}

    # chain len
    for i in range(1, n):
        # start position of the chain
        for j in range(0, n-i):

            best = float('inf')

            # split chain
            for k in range(j, j+i):

                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[k+1, j+i]
                cost = lcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                
                if cost < best:
                    aux[j, j+i] = cost, var, lrow, rcol

    return dict(zip(['cost', 'order', 'rows', 'cols'], aux[0, n-1]))

chain = [('A', 10, 20), ('B', 20, 30), ('C', 30, 40)]
print (mult(chain))

