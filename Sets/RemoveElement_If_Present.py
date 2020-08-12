setEx=set()

def removeElement(mySet,value):
    """
    remove the element in the set
    :param mySet: set
    :param value: value to be added in the set
    :return: return the updated set
    """
    if value in mySet:
        mySet.remove(value)
        print("Successfully removed",value,"from the set")
    else:
        print("No Such Element in the set")
    return mySet

size=(int(input("Enter the size of the size ")))
for i in range(size):
    setEx.add(int(input("Enter the unique elements in set ")))

print("Before removing the element",setEx)
element=(int(input("Enter the element to remove from the set ")))
print("After removing the element",removeElement(setEx,element))
