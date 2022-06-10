def findsend(array):
    largest=array[0]
    second=array[0]

    for i in range(len(array)):
        if array[i]>largest:
            largest= array[i]
    
    for i in range(len(array)):
        if array[i] >second and array[i]<largest:
            second=array[i]
    
    return second

array=[2,5,7,1,9,8,10]
print(findsend(array))

        