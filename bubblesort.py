def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                t = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t

data = [10,5,89,3,10]
bubblesort(data)
print("sorted array in asc order:")
print(data)
