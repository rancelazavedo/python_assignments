def sortVal(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n):
            if(arr[i]<arr[j]):
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            print(arr)
        print(i)


    return arr



arr =[6,7,3,4,2,9]

print("unsorted:")
print(arr)

sortVal(arr)

print("sorted:")
print(arr)

