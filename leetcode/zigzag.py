s = "PAYPALISHIRING"

def convert(s, nRows):
    cycle = 2 * nRows - 2
    res = []
    n = len(s)

    if (nRows == 1) or (nRows > n): # avoid Time Limit Exceeded
        return s

    for i in range(nRows):
        j = 0
        while j + i < n:
           res.append(s[i+j])

           if (i != 0) and (i != nRows- 1) and (j + cycle - i < n):
               res.append(s[j+cycle-i])

           j += cycle
    return ''.join(res)

print(convert(s, 4))
