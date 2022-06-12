def target_matrix(mat,n,x):
    row=0
    column=n-1
    while row<n and column >=0:
        if mat[row][column]==x:
            return (row,column)
        elif mat[row][column] < x:
            row+=1
        else:
            column-=1

mat=[[1,2,3],
    [4,5,6],
    [7,8,9]]
n=3
x=9
print(target_matrix(mat,n,x))