# program to convert list to tuples
demoList=[] #creates empty list

size=(int(input("Enter the size of the list ")))

#loop to add items in list
for i in range(size):
    demoList.append(input("Enter the integers value in list "))

tupleEx=tuple(demoList) #coverts list to tuple and then assigns to tupleEx
print("Converted list to tuple",tupleEx)