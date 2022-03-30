#Given a base-10 integer, n , convert it to binary (base-2). 
# Then find and print the base-10 integer denoting the maximum number of 
# consecutive 1's in n's binary representation. When working with different bases, 
# it is common to show the base as a subscript.

from numpy import binary_repr


number=int(input())
binary=[]
while number>=1:
    temp=number%2
    number//=2
    binary.append(temp)

count=result=0

for i in range(len(binary)):
    if binary[i]==0:
        count=0
    else:
        count+=1
        result=max(result,count)

print(result)