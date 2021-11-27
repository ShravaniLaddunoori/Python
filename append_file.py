fname = input('Enter file name:')
f1 = open(fname,'a')
str = input('Enter string to append:')
f1.write('\n')
f1.write(str)
f1.close()
print('Contents of appended file is:')
f2=open(fname,'r')
line = f2.readline()
while(line!=""):
    print(line)
    line=f2.readline()
f2.close()
























