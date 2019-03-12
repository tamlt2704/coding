from collections import defaultdict
import sys


def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height-1, left, middle, right)
        topdisk = d[left].pop(-1)
        d[right].append(topdisk)
        print("\n")
        print(left, "=>", right)
        cols = ['left', 'middle', 'right']

        print(str(dict(zip(cols, [d[col] for col in cols]))))
        hanoi(height-1, middle, right, left)


n = 3 if len(sys.argv) < 2 else int(sys.argv[1])

d = defaultdict(list)
d['left'] = list(range(1, n+1)[::-1])
d['right'] = []
d['middle'] = []
hanoi(n)
