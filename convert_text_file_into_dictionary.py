# txt file is in the same directory where the code is 

def convert_dict():
  dict={}
  file= open("textfile.txt")
  for i in file:
    x=i.split()
    dict[x[0]]= x[1:]
  
  return dict 

print(convert_dict)
   
