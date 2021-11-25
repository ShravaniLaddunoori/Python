result=i = 0
num = int(input('enter a number:'))
x = num
temp = num
while num!=0:
    num = num//10
    i = i+1
while temp!=0:
    num = temp%10
    result = result+pow(num,i)
    temp = temp//10
if (x==result):
    print('%d is armstrong number'%x)
else:
    print('%d is not armstrong number'%x)

