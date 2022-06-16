# from the given input of any rendom datatype of elements this function 
# will return the largest integet value

#  give your inputs: 2,3,4,"gy,2
#  (['2', '3', '4', '"gy'], 4)

def convertlist(a):
  array=[]
  result=""
  maxm= -float("inf")
  for i in a:
    if i!=",":
      result+=i
    else:
      array.append(result)

      try:
        int(result)
      except:
        pass
      else:
        result= int(result)
        if int(result) > maxm:
          maxm= int(result)

      result=""
  return array,maxm

a= input("give your inputs: ")
convertlist(a)

