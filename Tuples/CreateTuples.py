# program to create a tuple
demoList=[] #creates empty list

size=(int(input("Enter the size of the tuples ")))

#loop to add items in list
for i in range(size):
    demoList.append(input("Enter the value in list "))

tupleEx=tuple(demoList) #coverts list to tuple and then assigns to tupleEx
print(tupleEx)