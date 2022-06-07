def binarysearch(array,target):
    i=0
    y=len(array)-1
    while i!=y:
        mid=(i+y)//2
        if target==array[mid]:
            print("the targer is in that list")
            print(mid)
            break
        elif target<array[mid]:
            y=mid
        elif target>array[mid]:
            i=mid
        else:
            print("the target is not in the array")
            break

a=[1,2,3,4,5,6,7,8,8]
target=3
binarysearch(a,target)
