def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
    
print(selectionSort([7,9,5,4,8,1]))