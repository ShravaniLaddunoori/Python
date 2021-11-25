temp=0
num = int(input('Enter a number:'))
for i in range(2,num//2):
    if num%i==0:
       temp=1
       break
if temp==1:
        print('%d is not prime num'%num)
else:
        print('%d is prime num'%num)
