n = int(input('Enter num:'))
try:
    k = n//0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')
