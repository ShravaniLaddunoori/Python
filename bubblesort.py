def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [15,22,96,32,4,67,10,5,73]
print('Array is:')
for i in range(len(arr)):
    print('%d'%arr[i])

bubblesort(arr)

print('Soretd array is:')
for i in range(len(arr)):
    print('%d'%arr[i])
