input_str = input('Enter list elements:')
list = input_str.split()
print('List : ',list)
for i in range(len(list)):
    list[i]=int(list[i])
print('Largest num:',max(list))
