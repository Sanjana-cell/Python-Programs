#Program to add members in set

setEx=set()
def addElement(mySet,value):
    """
    add the element in the set
    :param mySet: set
    :param value: value to be added in the set
    :return: return the updated set
    """
    mySet.add(value)
    return mySet

size=(int(input("Enter the size of the size ")))
for i in range(size):
    setEx.add(int(input("Enter the unique elements in set ")))

print("Before adding the element",setEx)
element=(int(input("Enter the element to add in the set ")))
print("After adding the element",addElement(setEx,element))
