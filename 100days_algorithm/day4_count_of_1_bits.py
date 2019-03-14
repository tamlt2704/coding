def count_of_1bits(value):
    n = 0
    while value:
        print('value   = {0:b}'.format(value))
        print('value-1 = {0:b}'.format(value-1))
        value &= value -1
        n+=1
    return n

print(count_of_1bits(0b11001100))

