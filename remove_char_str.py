string = input('Enter a string:')
pos = int(input('Enter position to remove character:'))
new_str = string[:(pos-1)] + string[(pos+1):]
print(new_str)
