def mergemain(arr):
  count=0
  return mergeSort(arr,count)

def mergeSort(arr,count):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L,count)
    mergeSort(R,count)
  
    i = j = k = 0  
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
        k += 1
      else:
        arr[k] = R[j]
        count+=1
        j += 1
        k += 1

    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
  
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

    return count

arr=[2,3,1]
mergemain(arr)
