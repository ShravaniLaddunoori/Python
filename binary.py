n = int(input('Enter num:'))
x = []
while(n>0):
    digits = n%2
    x.append(digits)
    n = n//2
x.reverse()
print('Binary equivalent is:')
for i in x:
    print(i,end="")
print("")
