def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i, len(arr)):
            if arr[min]>arr[j]:
                min=j
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    return arr