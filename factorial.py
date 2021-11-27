num = int(input('Enter a number:'))
fact =1
if num<0:
    print('Factorial doesnot exist for negative numbers')
elif num==0:
    print('Factroial of 0 is 1')
else:
    for i in range(1,num+1):
        fact = fact*i
    print('Factorial of',num,'is:',fact)
