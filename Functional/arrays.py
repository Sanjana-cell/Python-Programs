#Program print 2D array
value=1
#infinte loop
while value==1:
    rows=(int(input("Enter the rows ")))
    colums=(int(input("Enter the no of columns ")))
    matrix=[]
    #loops till i reaches rows
    for i in range(rows):
        temp=[]
        for j in range(colums):
            temp.append(int(input("Enter the values in row ")))
        matrix.append(temp)

    #to print the 2d array
    for i in range(rows):
        for j in range(colums):
            print(matrix[i][j],end=" ")
        print(" ")
    break