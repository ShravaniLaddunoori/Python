fname = input('Enter file name:')
for line in reversed(list(open(fname))):
    print(line.rstrip())
