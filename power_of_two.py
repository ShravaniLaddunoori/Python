def ispoweroftwo(n):
    if(n==0):
        return False
    while(n!=1):
        if(n%2!=0):
            return False
        n = n//2
    return True

n = int(input('Enter a number:'))
if ispoweroftwo(n):
    print('YES')
else:
    print('NO')
