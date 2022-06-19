def longestpalindrom(string):
  result=[]
  for i in range(len(string)):
    
    #for the even length palindrom
    
    l=r=i
    while l>=0 and r<len(string):
      if string[l]==string[r]:
        if len(string[l:r+1])>2:
          result.append(string[l:r+1])
        l-=1
        r+=1
      else:
        break
    
    #for odd length palindrom
    
    l,r=i,i+1
    while l>=0 and r<len(string):
      if string[l]==string[r]:
        if len(string[l:r+1])>2:
          result.append(string[l:r+1])
        l-=1
        r+=1
      else:
        break

  return result

string="abaabdqd"
longestpalindrom(string)
    
