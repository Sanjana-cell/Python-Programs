#Program to clear the sets
set_1=set()
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
print(set_1)
choice=input("Do you want to create the set ? Enter y for yes")
if choice == "y": #check if choice y if y then clears the set
    set_1.clear() #clear the set
    print("Cleared all elements")
    print(set_1)
else:
    print(set_1)