# this code is working properly

def comparearay(array):
  a=[]
  l=0
  while l <len(array):
    a.append(0)
    l+=1
  cent=(len(a)-1)//2
  x=0
  y=len(array)-1

  #while x<=y:

  for i in reversed(range(len(array))):

    if abs(array[x])>abs(array[y]):
      a[i]=array[x]**2
      x+=1

    else:
      a[i]=array[y]**2
      y-=1
  return a
  
print("000000000000000000000")
comparearay([-7,-4,-2,6,8,9])