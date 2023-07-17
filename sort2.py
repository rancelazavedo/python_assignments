def sortVal(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]<arr[j+1]):
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            print(arr)
        print(i)

    return arr



arr =[63,77,33,44,22,99]

print("unsorted:")
print(arr)

sortVal(arr)

print("sorted:")
print(arr)

