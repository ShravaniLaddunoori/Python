x = input('Enter file name:')
file = open(x,'r')
line = file.readline()
while(line!=""):
    print(line)
    line = file.readline()
file.close()
