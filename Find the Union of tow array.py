#  GFG question: Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays. 

def unionarray(array1,array2):
  a=0
  b=0
  result=[]
  while a<len(array1) and b<len(array2):
    if array1[a] == array2[b]:
      result.append(array1[a])
      a+=1
      b+=1
    else:
      result.append(array1[a])
      result.append(array2[b])
      a+=1
      b+=1

  while a<len(array1):
    result.append(array1[a])
    a+=1
  
  while b< len(array2):
    result.append(array2[b])
    b+=1

  return result

array1=[85, 25, 1, 32, 54, 6]
array2=[85, 2 ]

unionarray(array1,array2)
