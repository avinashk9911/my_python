#Q)create a function which takes in a sorted array with integer 
# values and returns another array which is square of all the integers and sorted in assending order


# rough work:

# def squaresort(array):
#     if len(array)<1:
#         return 0
#     else:
#         x=0

# a=[0 for _ in range(4)]
# print(a)

def squaresort(array):
    a=[0 for _ in array]

    x=0
    y=len(array)-1

    for i in reversed(range(len(array))):
        if abs(array[x])> abs(array[y]):
            a[i]=array[x]**2
            x+=1
        # elif abs(array[y])>abs(array[x]):
        else:
            a[i]=array[y]**2
            y-=1
    return print(a)

squaresort([-8,-6,-4,-2,3,4,8])