n = int(input('Enter number:'))
sum = 0
for i in range(1,n):
    if (n%i==0):
        sum = sum+i
if sum==n:
    print('Perfect num')
else:
    print('Not perfect num')

