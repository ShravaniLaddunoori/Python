first,second = 0,1
num = int(input('Enter num:'))
print('Fibonacci series of %d numbers are:'%num)
for i in range(0,num):
    if i<=1:
        result = i
    else:
        result = first+second
        first = second
        second = result
    print(result)

