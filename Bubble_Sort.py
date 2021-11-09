def bubbleSort(arr):
    Change=True
    while Change:
        Change=False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                temp=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
                Change=True
    return arr