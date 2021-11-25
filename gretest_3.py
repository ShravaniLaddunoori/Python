n1,n2,n3 = [int(n1) for n1 in input('Enter 3 values:').split()]
if (n1>n2 and n1>n3):
    res = n1
elif (n2>n3 and n2>n1):
    res = n2
elif (n3>n1 and n3>n2):
    res = n3
print("Gretest num is:%d"%res)
