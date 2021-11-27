num = int(input('Enter number:'))
count = 0
if num>0:
    while num!=0:
        num = num//10
        count = count+1
        continue
else:
    count=1
print('Total digits are:',count)
