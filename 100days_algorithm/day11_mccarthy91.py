def maccarthy91(n):
    k = 1
    while k:
        if n > 100:
            n -= 10
            k -= 1
        else:
            n += 11
            k += 1
    return n

def maccarthy91_rec(n):
    if n > 100:
        return n - 10
    else:
        return maccarthy91_rec(maccarthy91_rec(n+11))

print(maccarthy91(80))
print(maccarthy91(110))
