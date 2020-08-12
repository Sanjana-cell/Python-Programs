set_1=set()
set_2=set()
def createSet():
    """
    creates the set
    :return: returns the set
    """
    mySet=set()
    size=(int(input("Enter the size of the size ")))
    for i in range(size):
        mySet.add(int(input("Enter the unique elements in set ")))
    return mySet
def addElement(mySet,value):
    """
        add the element in the set
        :param mySet: set
        :param value: value to be added in the set
        :return: return the updated set
        """
    try:
        mySet.add(value)
    except:
        print("You cannot add element in this set becaues it is forzen set")
    return mySet

set_1=createSet()
set_2=frozenset(createSet())

print("Before adding the element")
print("Set 1",set_1)
element=(int(input("Enter the element to add in the set ")))
set_1=addElement(set_1,element)
print("After adding the element",set_1)

print("Before adding the element")
print("Set 2",set_2)
element=(int(input("Enter the element to add in the set ")))
set_2=addElement(set_2,element)
print("After adding the element",set_2)
