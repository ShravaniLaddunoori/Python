def set_bits(n):
    count = 0
    while n:
        n = n&(n-1)
        count = count+1
    return count
n = int(input('Enter num:'))
print('Number of set bits:',set_bits(n))
