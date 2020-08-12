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

set_1=createSet()
set_2=createSet()
print("Set 1",set_1)
print("Set 2",set_2)
print("Difference of the Set_1 - Set_2",set_1.difference(set_2))
print("Difference of the Set_2 - Set_1",set_2.difference(set_1))