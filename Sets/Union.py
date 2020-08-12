#Program to create union of two sets
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
print(set_1)
print(set_2)
print("Union of the Sets",set_1.union(set_2)) #prints union of the sets