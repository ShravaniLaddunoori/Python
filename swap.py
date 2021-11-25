a = int(input('Enter a value:'))
b = int(input('Enter b value:'))
print("Before swap a:{0} b:{1}".format(a,b))
a = a+b
b = a-b
a = a-b
print("After swap a:{0} b:{1}".format(a,b))

