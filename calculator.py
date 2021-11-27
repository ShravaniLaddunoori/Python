def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
print('Enter two numbers:')
n1=input()
n2=input()
print('Enter the operation (+,-,*,/):')
op=input()
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    sub(int(n1),int(n2))
elif op=='*':
    mul(int(n1),int(n2))
elif op=='/':
    div(int(n1),int(n2))
else:
    print('Invalid operation')

