fname = input('Enter file name:')
count = 0
with open(fname,'r') as f:
    for line in f:
        words = line.split()
        count += len(words)
print('No of words:',count)
