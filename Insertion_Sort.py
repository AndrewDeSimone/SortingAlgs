def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
    return arr