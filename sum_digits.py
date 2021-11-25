sum=0
num = int(input('Enter a number:'))
while num!=0:
    x = num%10
    sum =sum+x
    num = num//10
print('Digits sum:%d'%sum)

