start = int(input('Enter starting range:'))
end = int(input('Enter ending range:'))
print('prime nums between',start,'and',end,'are:')
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
