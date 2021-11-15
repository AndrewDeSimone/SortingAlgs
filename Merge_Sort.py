def mergeSort(arr):
    if len(arr)==1:
        return arr
    arrL=arr[:len(arr)//2]
    arrR=arr[len(arr)//2:]
    return merge(mergeSort(arrL), mergeSort(arrR))

def merge(arrL, arrR):
    arr=[]
    counterL=0
    counterR=0
    while counterL<len(arrL) and counterR<len(arrR):
        if arrL[counterL]<arrR[counterR]:
            arr.append(arrL[counterL])
            counterL+=1
        else:
            arr.append(arrR[counterR])
            counterR+=1
    while counterL<len(arrL):
        arr.append(arrL[counterL])
        counterL+=1
    while counterR<len(arrR):
        arr.append(arrR[counterR])
        counterR+=1
    return arr

arr = [1,7,3,6,8,9,10]
print(mergeSort(arr))