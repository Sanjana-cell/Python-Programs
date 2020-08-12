# program to remove an item from a tuple
demoList=[] #creates empty list

def removeItem(myTuple,value):
    """
    removes an item in list and return updated tuple
    :param myTuple: tuples
    :param value: element to be removed from tuple
    :return: return updated tuples
    """
    myList=list(myTuple) #converts tuple to list to do deletion operation
    for x in myList:
        # checks if value is there in myList , it is required to avoid exception
        if value in myList:
            myList.remove(value)
            print("Deleted Successfully")
    myTuple=tuple(myList) #converts list to tuples
    return myTuple

size=(int(input("Enter the size of the list ")))

#loop to add items in list
for i in range(size):
    demoList.append(input("Enter the integers value in list "))

tupleEx=tuple(demoList) #coverts list to tuple and then assigns to tupleEx
print(tupleEx)
element=(input("Enter the value to be deleted"))
print("After deleting element from tuple",removeItem(tupleEx,element)) #function call and printd the updated tuples