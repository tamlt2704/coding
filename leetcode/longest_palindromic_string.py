s = "cbbd"
s = "kiomaramol"
s = "babad"
s = "cbbd"
q = f'#{"#".join(list(s))}#'
p = [0 for _ in range(len(q))]
n = len(q)


c, r, = 0, 0

for i in range(1, len(q)):

    iMirror = c - (i-c)

    if i < r:
        p[i] = min(p[iMirror], r - i)
    
    i1, i2 = i+p[i], i-p[i]
    while (i1 < (n-1)) and (i2 > 0) and (q[i1 + 1] == q[i2 - 1]):
        p[i] += 1
        i1, i2 = i+p[i], i-p[i]

    if i + p[i] > r:
        c = i
        r = i + p[i]
    

#print(' '.join(map(str, q)))
#print(' '.join(map(str, p)))

# find longest
maxLen = 0
center = 0
for i in range(0, n):
    if p[i] > maxLen:
        maxLen = p[i]
        center = i

s = s[(center - maxLen)//2+1: (center+maxLen)//2+1]
print(s)
