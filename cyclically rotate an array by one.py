def rotate(array):
  i=0
  j=len(array)-1
  while i!=j:
    array[i],array[j]=array[j],array[i]
    i+=1
  return array

array=[1, 2, 3, 4, 5]
rotate(array)
